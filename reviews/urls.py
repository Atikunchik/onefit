from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.review_list, name='review_list'),
    url(r'^add_review/$', views.add_review, name='add_review'),
    url(r'^login/$', views.login_user, name='login'),
]