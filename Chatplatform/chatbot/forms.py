from django import forms
from .models import Chatbot


class ChatbotForm(forms.ModelForm):
    class Meta:
        model = Chatbot
        fields = ('query', 'response')