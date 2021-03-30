from django.shortcuts import render
from .models import Resume

# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    resume=Resume.objects.get(pk=1)
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')