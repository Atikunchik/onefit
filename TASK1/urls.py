from django.urls import include, path
from rest_framework import routers
from accounts import views
from reviews import views
from django.contrib import admin
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url('reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
    url('login/', include(('accounts.urls', 'accounts'), namespace='accounts')),
]