from django.shortcuts import render

#dummy data
posts = [
    {
    'pitch_title': 'pitch post 1',
    'creater':'Terry Tsai',
    'description':'First pitch description',
    'date_posted':'March 9,2019',
    },
    {
    'pitch_title': 'pitch post 2',
    'creater':'Jeff Hicks',
    'description':'Second pitch description',
    'date_posted':'March 10,2019',
    }
]

# Create your views here.
def home(request):
    #set up a dictionary
    context = { ##key value pair
        'posts': posts
    }
    return render(request,'pitch/home.html',context)

def about(request):
    return render(request,'pitch/about.html',{'pitch_title':'About'})
