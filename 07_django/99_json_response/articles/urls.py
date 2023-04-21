from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_json),
]
