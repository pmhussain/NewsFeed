from django.forms import ModelForm
from .models import *

class PersonForm(ModelForm):
    class Meta:
        model = Message
        #fields = ['message', 'image']
        fields = '__all__'
        exclude = ['user']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message', 'image']
        #fields = '__all__'
