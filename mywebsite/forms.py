from django import forms 
from mywebsite.models import Contact
# from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'