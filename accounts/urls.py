from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_user, name='login_user'),
]