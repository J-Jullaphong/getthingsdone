from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..forms import CustomUserCreationForm


class SignUpView(CreateView):
    """This view is for handling user registration."""
    model = User
    form_class = CustomUserCreationForm
    template_name = 'todo/signup.html'
    success_url = reverse_lazy('todo:todo_list')

    def form_valid(self, form):
        """
        This method is called when the submitted form is valid.
        It saves the user, logs them in, and redirects to the todo list.
        """
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
