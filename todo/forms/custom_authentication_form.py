from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    """
    Extends Django's default AuthenticationForm to apply Bootstrap styling
    to each visible field.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Enter your username',
            'password': 'Enter your password',
        }

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name in placeholders:
                visible.field.widget.attrs['placeholder'] = placeholders[
                    visible.name]
