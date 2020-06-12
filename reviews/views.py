from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from TASK1.serializers import UserSerializer, GroupSerializer
from django.shortcuts import get_object_or_404, render
from .models import Review


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def review_list(request):
    latest_review_list = Review.objects.all()
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/reviews_list.html', context)



