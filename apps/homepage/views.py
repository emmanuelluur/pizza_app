from django.shortcuts import render

# Create your views here.


def home_view(request):
    template = "homepage.html"
    context = {}
    return render(request, template, context)