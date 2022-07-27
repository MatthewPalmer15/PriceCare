from django.shortcuts import render

def index(request):
    """ Render the home page """
    return render(request, "main/index.html", {})

def about(request):
    """ Render the about page """
    return render(request, "main/about.html", {})

def contact(request):
    """ Render the contact page """
    return render(request, "main/contact.html", {})

def policy(request):
    """ Render the policy page """
    return render(request, "main/policy.html", {})
