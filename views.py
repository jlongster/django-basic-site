from django.shortcuts import render_to_response
from django.contrib.auth import forms

def index(request):
    return render_to_response('test.html',
                              { 'user_form': forms.AuthenticationForm()})
