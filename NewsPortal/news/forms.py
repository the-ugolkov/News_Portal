from django import forms

from .models import Post, Category


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Post
        fields = ['author', 'title', 'text']
