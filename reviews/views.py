from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.utils import json

from TASK1 import serializers
from TASK1.serializers import UserSerializer, GroupSerializer
from django.shortcuts import get_object_or_404, render
from .models import Review, Company
from django.http import HttpResponse
from ipware import get_client_ip
from rest_framework import status


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


def del_rev(request, review_id):
    token = request.META.get('HTTP_AUTHORIZATION')
    user = User.objects.filter(auth_token=token).first()
    if user is None:
        return HttpResponse("Permission denied")
    user = User.objects.get(auth_token=token)
    review = get_object_or_404(Review, pk=review_id)
    if user.id != review.user.id and not user.is_superuser:
        return HttpResponse("Permission denied")
    Review.objects.filter(id=review_id).delete()
    return HttpResponse("deleting done", status=status.HTTP_200_OK)


def review_list(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    #is_routable = get_client_ip(request)
    user = User.objects.filter(auth_token=token).first()
    if user is None:
        return HttpResponse("Permission denied")
    user = User.objects.get(auth_token=token)
    #print(list(Review.objects.get(user=user)))
    latest_review_list = Review.objects.filter(user=user)
    if user.is_superuser:
        latest_review_list = Review.objects.all()
    #ip = is_routable.first()
    return HttpResponse(json.dumps({'latest_review_list': ([review.full() for review in latest_review_list.all()])}), content_type="application/json", status=status.HTTP_200_OK)


def add_review(request):
    print(request.META.get('HTTP_AUTHORIZATION'), "gettoken")
    token = request.META.get('HTTP_AUTHORIZATION')
    user = User.objects.filter(auth_token=token).first()
    print(token, "TOKEN HERE")
    print(user, "USER HERE")
    print(User.objects.all())
    if user is None:
        return HttpResponse("User Permission denied", status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        req = request.POST
        review = Review()
        print(Company.objects.all())
        company = Company.objects.filter(pk=req.get('company_id'))
        print(company.first(), "HERE COMPANY")
        if not company.exists():
            return HttpResponse("Company Error Message")
        review.company = company.first()
        review.rating = req.get('rating')
        review.title = req.get('title')
        review.description = req.get('description')
        review.user = user
        review.save()
        return HttpResponse(json.dumps({'review': review.full()}), content_type='application/json', status=status.HTTP_200_OK)
    return HttpResponse("1")
