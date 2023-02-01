from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post
# from ..NewsPortal import settings


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'author', 'title', 'text']


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        #
        # html_content = render_to_string(
        #     'post_created_email.html',
        #     {
        #         'text': "Добро пожаловать на NewsPortal",
        #         'link': f'{settings.SITE_URL}/news/',
        #     }
        # )
        #
        # msg = EmailMultiAlternatives(
        #     subject='Добро пожаловать',
        #     body='',
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     to=user.values('email'), #????
        # )
        #
        # msg.attach_alternative(html_content, 'text/html')
        # msg.send()

        return user
