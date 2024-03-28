from django import forms 
from news.models import Comments,Newsletter
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Comments
        fields = ['news','name','email','message']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']