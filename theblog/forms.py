from django import forms
from .models import Post, Category, Comment
from django.contrib.auth.models import User

# Hard code catogries not dynmic will not use for this use case
#choices = [('coding', 'coding'), ('writing', 'writing'), ('sports', 'sports'), ('entertainment', 'entertainment')]

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

sorted_choice_list = sorted(choice_list)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'snippet', 'body','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user_selector', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices= sorted_choice_list, attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'snippet','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices= sorted_choice_list, attrs={'class': 'form-control'}), #choices must be before attrs
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Comment
        fields = ( 'body',)

        def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)
