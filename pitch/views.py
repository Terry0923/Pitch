from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    #set up a dictionary
    context = { ##key value pair
        'posts': Post.objects.all()
    }
    return render(request,'pitch/home.html',context)

def about(request):
    return render(request,'pitch/about.html',{'pitch_title':'About'})
