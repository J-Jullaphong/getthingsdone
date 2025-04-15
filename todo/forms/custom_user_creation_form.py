from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    """
    Extends Django's UserCreationForm to apply Bootstrap styling
    to each visible field.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Choose a username',
            'password1': 'Create a password',
            'password2': 'Confirm your password',
        }

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name in placeholders:
                visible.field.widget.attrs['placeholder'] = placeholders[
                    visible.name]
