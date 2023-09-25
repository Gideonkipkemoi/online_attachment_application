from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} successfully created')
            return redirect("login")
    else:

        form = UserRegistrationForm()
    return render(request, 'register.html',{'form':form})

