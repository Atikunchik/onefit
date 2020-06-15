from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
import json


def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            check = Token.objects.filter(user=user).first()
            if check is None:
                token = Token.objects.create(user=user)
            else:
                token = Token.objects.get(user=user)
            return HttpResponse(json.dumps({'token': token.key}), content_type='application/json')
    return render(request, 'reviews/login.html', {'form': form})