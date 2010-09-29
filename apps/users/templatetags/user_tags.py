from django import template
from django.contrib.auth import forms
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

register = template.Library()

def login_form(parser, token):
    return LoginForm()
        
class LoginForm(template.Node):
    def __init__(self):
        self.form = forms.AuthenticationForm()
        
    def render(self, context):
        context['user_form'] = self.form
        context['post_url'] = reverse('users:login')
        return render_to_string('users/inline_form.html', context)


register.tag('login_form', login_form);
