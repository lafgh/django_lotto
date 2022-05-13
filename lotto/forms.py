from django import forms
from .models import GuessNumbers

# Django에서 제공하는 ModelForm을 활용해 form 구성
class PostForm(forms.ModelForm):

    # Form을 통해 받아들여야할 데이터가 명시되어 있는 메타 데이터 (DB 테이블을 연결)
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # 사용자로부터 form 통해 입력받을 데이터
