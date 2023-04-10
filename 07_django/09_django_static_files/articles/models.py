from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # MEDIA_ROOT 이후의 추가 경로를 설정 => upload_to
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
