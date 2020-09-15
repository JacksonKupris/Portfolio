from django import forms
from django.forms import ModelForm
from django.forms import models
from django.forms import widgets

from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }