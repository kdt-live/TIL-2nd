from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:artilce_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.comment_delete,
        name='comment_delete',
    ),
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
