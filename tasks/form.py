from django import forms

from tags.models import Tag
from tasks.models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'due_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            )
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['tags'].queryset = Tag.objects.filter(user=user)

