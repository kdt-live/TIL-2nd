from django.db import models
# 직접 참조는 비추천
# from accounts.models import User

# 이전에 배웠던 get_user_model 함수를 사용?? (models.py에서는 사용하지 않음)
# from django.contrib.auth import get_user_model

# models.py에서 User를 참조할때만 다음과 같이 참조한다.
from django.conf import settings


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # 외래 키 필드
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

