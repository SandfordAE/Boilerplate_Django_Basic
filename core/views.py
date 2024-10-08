from django.shortcuts import render
from django.http import HttpResponse 
from visits.models import PageVisit

def main_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "Main Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100 / qs.count()),
        "total_visit_count": qs.count(),
    }

    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)