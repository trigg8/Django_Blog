from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import EditForm, PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#def home(request):
#    return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-post_date']
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by('name')
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' ')).order_by('-id')
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all().order_by('name')
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

class ArticleDetailView(DetailView):
    model = Post 
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by('name')
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = current_post.total_likes()
        
        liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    
    
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)
    
    def get_success_url(self):
        post_id = self.object.post.id
        return reverse_lazy('article-detail', kwargs = {'pk': post_id})

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'

    def get_success_url(self):
        post_id = self.object.post.id
        return reverse_lazy('article-detail', kwargs = {'pk': post_id})

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    def get_success_url(self):
        post_id = self.object.post.id
        return reverse_lazy('article-detail', kwargs = {'pk': post_id})
    