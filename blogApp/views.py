from django.shortcuts import render
from . import models

# Create your views here.

def index(req):
    return render(req,'index.html')

def blog(req):
    context_list = models.BlogPost.objects.order_by('upload_time')
    return render(req,'BlogView.html',context={'data':context_list})

    
def blog_list(req):
    context_list = models.BlogPost.objects.order_by('upload_time')
    return render(req,'BlogList.html',context={'data':context_list})