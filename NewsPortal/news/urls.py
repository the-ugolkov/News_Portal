from django.urls import path
from .views import NewDetail, NewsList, SearchList, PostCreate, PostUpdate, PostDelete, CategoryList, subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('news/', cache_page(60)(NewsList.as_view()), name='post_list'),
    path('news/<int:pk>', cache_page(60 * 5)(NewDetail.as_view()), name='post_detail'),
    path('news/search/', SearchList.as_view(), name='post_search'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_create'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete', PostDelete.as_view(), name='articles_delete'),
    path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribers', subscribe, name='subscribe'),

]
