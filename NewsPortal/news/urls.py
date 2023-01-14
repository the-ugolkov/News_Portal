from django.urls import path
from .views import NewDetail, NewsList, SearchList, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>', NewDetail.as_view(), name='post_detail'),
    path('search/', SearchList.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_create'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
