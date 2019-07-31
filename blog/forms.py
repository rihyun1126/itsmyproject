from django import forms
from .models import Blog, Comment

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
    
        fields = ['comment_user', 'comment_textfield']
        widgets = {
            'comment_textfield' : forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }