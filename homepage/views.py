from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login

from .forms import CreateUserForm
# Create your views here.


def homepage_view(request):
    return render(request, 'homepage.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def register2(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)