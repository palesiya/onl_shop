from django.shortcuts import render
from django.http import HttpResponse
from home.forms import EmailForm


def about(request):
    form_email = request.session.get("email")
    email = EmailForm(initial=form_email) if form_email is not None else EmailForm()
    return render(request, "about.html", {"email": email})


