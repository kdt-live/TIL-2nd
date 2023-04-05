from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# django User 객체에 대한 직접 참조를 권장하지 않는다.
# from .models import User

# 대신 다음과 같은 함수를 제공한다.
# get_user_model은 현재 프로젝트에 활성화 되어있는 User 객체를 반환해준다.
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 우리가 사용하는 User class로 재정의
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)

