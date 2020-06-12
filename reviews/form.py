from django.forms import ModelForm, Textarea
from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['username', 'rating', 'title']
        widgets = {
            'comment': Textarea(attrs={'cols': 30, 'rows': 15})
        }
