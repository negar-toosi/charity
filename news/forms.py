from django import forms 
from news.models import Comments
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Comments
        fields = ['news','name','email','message']