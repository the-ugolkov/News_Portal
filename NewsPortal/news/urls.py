from django.urls import path
from .views import NewDetail, NewsList, SearchList


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewDetail.as_view()),
    path('search/', SearchList.as_view()),
]
