from django import forms
from tags.models import Tag


class TagModelForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        exclude = ['user']


