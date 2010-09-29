from django.contrib.auth import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UserRegistrationForm

def login(request):
    if request.method == 'POST':
        # If you pass the request to the constructor as the first
        # argument, it will check it to make sure cookies are enabled.
        # For now, we assume it.
        form = forms.AuthenticationForm(None, request.POST)

        if form.is_valid():
            form = None
    else:
        form = forms.AuthenticationForm()

    return render_to_response('users/login.html',
                              RequestContext(request, { 'user_form': form,
                                                        'page': 'login'}))

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form = None
    else:
        form = UserRegistrationForm()

    return render_to_response(
        'users/register.html',
        RequestContext(request, { 'form': form,
                                  'page': 'register' })
        )
