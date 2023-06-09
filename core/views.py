from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signUp(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('core:frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signUp.html', {'form': form})


def loginPage(request):
    return render(request, 'core/login.html')
