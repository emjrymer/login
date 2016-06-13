import json
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView, View

from django.http import HttpResponseRedirect, HttpResponse


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login_view")


class WhatView(TemplateView):
    template_name = "what.html"


class AwesomeAPIView(View):

    def get(self, request):
        # Awesome.objects.all()
        print(request.user)
        data = json.dumps({"joel": "awesome"})
        return HttpResponse(data, content_type="application/json")

def homepage(request):
    return HttpResponseRedirect(reverse('login_view'))
