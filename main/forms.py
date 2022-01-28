from . models import Message
from django import forms


class MessageForm(forms.Form):
    author_name = forms.CharField(max_length=50, label='Your name', required=True)
    message_text = forms.CharField(widget=forms.Textarea, label='Message', required=True)