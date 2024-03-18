from django.shortcuts import render
from mywebsite.forms import ContactForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request,'mywebsite/index.html')

def donate_view(request):
    return render(request,'mywebsite/donate.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.name = 'unknown'
            instance = form.save(commit=False)
            if not form.cleaned_data['subject']:
                instance.subject = None  # Setting subject to None explicitly
            instance.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submited successfully')
    
    form = ContactForm()
    return render( request,'mywebsite/contact.html',{'form':form})

def about_view(request):
    return render(request,'mywebsite/about.html')