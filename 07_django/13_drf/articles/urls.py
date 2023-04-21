from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
]
