from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
            'movieTitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie title'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter director name'}),
            'review_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter review'}),
            'ratings': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reviewer_emailId': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter reviewer email'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'genres': forms.Select(attrs={'class': 'form-control'}),
        }


