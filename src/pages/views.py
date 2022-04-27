from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return render(request, "home.html", {})


def contact_view(request, *args, **kargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kargs):
    my_context = {
        "title": "this is the new titleo",
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [42351,3452,"holiii",42222],
        "my_html": "<h1>hello world</h1>"
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kargs):
    return render(request, "social.html", {})
