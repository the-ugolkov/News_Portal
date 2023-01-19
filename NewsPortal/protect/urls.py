from django.urls import path

from .views import IndexView, upgrade_me

urlpatterns = [
    path('accounts/', IndexView.as_view(), name='account'),
    path('accounts/upgrade/', upgrade_me, name='upgrade'),
]
