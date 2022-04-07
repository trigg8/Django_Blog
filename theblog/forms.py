from django import forms
from .models import Post, Category

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
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices= sorted_choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices= sorted_choice_list, attrs={'class': 'form-control'}), #choices must be before attrs
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
