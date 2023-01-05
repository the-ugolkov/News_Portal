from django.urls import path
from .views import NewDetail, NewsList


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewDetail.as_view()),
]
