from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Authorization
from .forms import *


def index(request):
    if is_session(request):
        return redirect('list')
    form = AuthorizationForm()

    context = {'form': form}

    return render(request, 'authorization/index.html', context)


def path_reg(request):
    form = RegistrationForm()

    context = {'form': form}

    return render(request, 'authorization/registration.html', context)


@require_POST
def authorize(request):
    form = AuthorizationForm(request.POST)

    if form.is_valid():
        current = Authorization.objects.filter(user=request.POST['user'], password=request.POST['password'])
        if current:
            request.session.setdefault('user', request.POST['user'])
            request.session.setdefault('password', request.POST['password'])
            return redirect('user/')
        else:
            return redirect('index')


@require_POST
def registrate(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        new_user = Authorization(**form.cleaned_data)
        new_user.save()

    return redirect('index')


def is_session(request):
    if request.session.get('user', None):
        if Authorization.objects.filter(user=request.session['user'], password=request.session['password']):
            return True
    return False
