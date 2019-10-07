from django import forms
from .models import GuessNumbers

class PostForm(form.ModelForm):
    class Meta:
        model = GuessNumbers #어떤 모델 쓸래
        field = ('name','text',) #뭐 입력받을래