from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # 데이터 조회에 대한 URL 패턴
    path('<int:pk>/', views.detail, name='detail'),
    # 데이터 수정 페이지에 대한 URL 패턴
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    # 데이터 삭제에 대한 URL 패턴
    path('<int:artilce_pk>/delete/', views.delete, name='delete'),
    # 데이터 수정 로직에 대한 URL 패턴
    path('<int:article_pk>/update/', views.update, name='update'),
]


# 메인 주소 articles/
# 상세 페이지 주소 articles/1/
