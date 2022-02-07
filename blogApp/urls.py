from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name="index"),
    path('blog/',views.blog,name="blog"),
    path('bloglist/',views.blog_list,name="bloglist")
]
