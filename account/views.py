from django.views.generic import FormView
from account.forms import LoginForm, UserRegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.shortcuts import redirect, render


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.cleaned_data.get("user"))
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        return reverse('home')


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})