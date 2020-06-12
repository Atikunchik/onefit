from django.forms import ModelForm, Textarea
from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 30, 'rows': 15})
        }
    def validrate(self):
        rating = self.cleaned_data.get('rating')
        if rating > 5 or rating < 1:
            return rating
        else:
            raise ReviewForm.ValidationError('rating is not valid')
