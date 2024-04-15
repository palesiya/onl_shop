from django.http import HttpResponseRedirect
from django.views.generic import FormView
from review.forms import ReviewForm
from home.forms import EmailForm
from django.shortcuts import render
from review.models import Review


def review_email(request):
    email = EmailForm()
    review = ReviewForm()
    reviews = Review.objects.all()[1::2]
    if request.method == 'POST':
        email = EmailForm(request.POST)
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()
            return HttpResponseRedirect(request.headers.get("Referer" or "/"))
        if email.is_valid():
            email.save()
            return HttpResponseRedirect(request.headers.get("Referer" or "/"))
    return render(request, 'review.html', {"review": review, "email": email, 'reviews': reviews})


