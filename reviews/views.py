from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from TASK1.serializers import UserSerializer, GroupSerializer
from django.shortcuts import get_object_or_404, render
from .models import Review
from .form import ReviewForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.utils import timezone


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


class DetailView(generic.DetailView):
    model = Review
    template_name = 'reviews/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Review.objects.all()


def del_rev(request, review_id):
    print("work")
    token = request.headers['Authorization']
    user = User.objects.filter(auth_token=token).first()
    if user is None:
        return HttpResponse("Permission denied")
    user = User.objects.get(auth_token=token)
    print(user.username)
    review = get_object_or_404(Review, pk=review_id)
    print(review.user.id)
    print(user.id != review.user.id)
    print(user.is_superuser)
    if user.id != review.user.id and not user.is_superuser:
        return HttpResponse("Permission denied")
    Review.objects.filter(id=review_id).delete()
    return HttpResponse("deleting done")



def review_list(request):
    token = request.headers['Authorization']
    user = User.objects.filter(auth_token=token).first()
    if user is None:
        return HttpResponse("Permission denied")
    user = User.objects.get(auth_token=token)
    latest_review_list = Review.objects.filter(user=user)
    if user.is_superuser:
        latest_review_list = Review.objects.all()
    # print(user.username)
    context = {'latest_review_list': latest_review_list, 'user': user}
    return render(request, 'reviews/reviews_list.html', context)


def add_review(request):
    token = request.headers['Authorization']
    user = User.objects.filter(auth_token=token).first()
    if user is not None:
        print(user)
    else:
        return HttpResponse("Permission denied")
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'reviews/addreviews.html', {'form': form})
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.save()
            return redirect('http://127.0.0.1:8000/reviews/')
        return render(request, 'reviews/addreviews.html', {'form': form})


