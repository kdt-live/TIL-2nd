from django.urls import path
from . import views


urlpatterns = [
    path('index-1/', views.index_1),
    path('index-2/', views.index_2),
    path('index-3/', views.index_3),
    path('index-4/', views.index_4),
]
