
from django.shortcuts import render
from django.views.generic import FormView
from home.forms import EmailForm
from django.http import HttpResponseRedirect


def home_email(request):
    email = EmailForm()
    if request.method == 'POST':
        email = EmailForm(request.POST)
        if email.is_valid():
            email.save()
            return HttpResponseRedirect(request.headers.get("Referer" or "/"))
    return render(request, 'home.html', {"email": email})
