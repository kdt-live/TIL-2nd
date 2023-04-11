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
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]

# 몇 번 댓글을 삭제해야 하는지 (댓글 조회) => 댓글을 조회할 pk를 받아야 함
# 댓글이 삭제된 이후 detail 페이지로 redirect => 몇번 게시글의 detail?? => 게시글을 조회할 pk도 필요
