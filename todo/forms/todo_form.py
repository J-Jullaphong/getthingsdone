from django import forms

from ..models import Todo


class TodoForm(forms.ModelForm):
    """A model-based form for creating and updating Todo items."""

    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'image', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title',
                'autofocus': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Add some details',
                'rows': 3,
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            },
                format='%Y-%m-%dT%H:%M'
            ),
        }
