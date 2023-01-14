from django.urls import path
from .views import NewDetail, NewsList, SearchList, PostCreate

urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>', NewDetail.as_view(), name='post_detail'),
    path('search/', SearchList.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
]
