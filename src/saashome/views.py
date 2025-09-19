from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home_view(request, *args, **kwargs):
    return about_View(request,*args,**kwargs)


def about_View(request, *args, **kwargs):
    queryset= PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    mytitle="My Page"
    mycontext={
        "Page Title": mytitle,
        "page_visit_count": page_qs.count,
        "total_visit_count": queryset.count
    }
    PageVisit.objects.create(path=request.path)

    
    return render(request, "home.html",mycontext)