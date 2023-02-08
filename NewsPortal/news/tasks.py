from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Category, Post


# @shared_task
# def send_message():
#     post = Post
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
#             'post': post,
#             'text': post.text,
#             'link': f'{settings.SITE_URL}/news/{post.pk}',
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=f'{post.title}',
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=Category.subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()

# @shared_task
# def send_message(pk_, id_cat):
#     post = Post.objects.get(id=pk_)
#     emails = User.objects.filter(categories__id__in=id_cat).values('email').distinct()
#     emails_list = [item['email'] for item in emails]
#     html_content = render_to_string(
#         'email_create.html',
#         {
#             'Post': post
#         }
#     )
#     msg = EmailMultiAlternatives(
#         subject=f'{post.header}',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=emails_list
#     )
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()

@shared_task
def send_message(post):
    email_list = []
    subscribes = User.categories.all()
    email_list += [s.email for s in subscribes]
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': post.text,
            'link': f'{settings.SITE_URL}/news/{post.pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=post.title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=email_list,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
