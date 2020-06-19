from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
import json


def login_user(request):
    if request.method == 'GET':
        return HttpResponse("what front need")
    else:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return HttpResponse("wrong username or password", status=status.HTTP_400_BAD_REQUEST)
        check = Token.objects.filter(user=user).first()
        if check is None:
            token = Token.objects.create(user=user)
        else:
            token = Token.objects.get(user=user)
        return HttpResponse(json.dumps({'token': token.key}), content_type='application/json', status=status.HTTP_200_OK)
