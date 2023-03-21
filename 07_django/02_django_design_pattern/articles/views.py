from django.shortcuts import render

# Create your views here.
# 특정 기능을 수행하는 view 함수들을 작성
# 모든 view 함수는 첫번째 인자로 요청 객체를 필수적으로 받는다./
def index(request):
    return render(request, 'articles/index.html')
