from django import forms
from .models import Article

 
class ArticleForm(forms.ModelForm):
    # 필드 커스텀(재정의)
    title = forms.CharField(
        label='제목',
        help_text = '제목을 입력해주세요',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목',
            }
        ),
    )

    class Meta:
        model = Article
        fields = '__all__'
