from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "title": "Home",
    }
    return render(request, "home.html", my_context)


def contact_view(request, *args, **kargs):
    my_context = {
        "title": "Contact",
    }
    return render(request, "contact.html", my_context)


def about_view(request, *args, **kargs):
    my_context = {
        "title": "About",
        "my_text": "This is about us",
        "my_number": "625-847-586",
        "my_list": [42351,3452,"holiii",42222],
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kargs):
    return render(request, "social.html", {})
