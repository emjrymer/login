from django.conf.urls import url
from django.contrib import admin
from app.views import homepage, SignUpView, WhatView, AwesomeAPIView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage),
    url(r'^what/$', WhatView.as_view(), name="what_view"),
    url(r'^api/awesome/$', AwesomeAPIView.as_view(), name="awesome_api_view"),
    url(r'^signup/$', SignUpView.as_view(), name="signup_view"),
    url(r'^login/$', auth_views.login, name="login_view"),
    url(r'^logout/$', auth_views.logout_then_login, name="logout_view"),
]
