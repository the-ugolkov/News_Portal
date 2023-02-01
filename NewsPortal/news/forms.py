from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'author', 'title', 'text']


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)

        return user
