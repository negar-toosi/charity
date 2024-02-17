from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'mywebsite/index.html')

def donate_view(request):
    return render(request,'mywebsite/donate.html')