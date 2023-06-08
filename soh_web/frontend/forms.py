from django import forms
from .models import OrderOrQuestion

class OrderOrQuestionForm(forms.ModelForm):
    class Meta:
        model = OrderOrQuestion
        fields = ['question', 'name', 'phone', 'email', 'city']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
        }
        labels = {
            'question': 'Ваш вопрос',
            'name': 'Имя',
            'phone': 'Телефон',
            'email': 'Электронная почта',
            'city': 'Город',
        }