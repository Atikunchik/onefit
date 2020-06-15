from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.review_list, name='review_list'),
    url(r'^add_review/$', views.add_review, name='add_review'),
    url(r'^(?P<review_id>\w+)/$', views.del_rev, name='delete_review'),
]