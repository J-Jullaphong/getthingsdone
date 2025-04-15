from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..forms import TodoForm
from ..models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    """
    This view is for displaying the todo dashboard.
    It shows all todo items belonging to the current user, grouped by status.
    """
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    login_url = 'todo:login'

    def get_queryset(self):
        """Returns a queryset of todo items filtered by the currently logged-in user."""
        return Todo.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        """
        Adds additional context for the template, including:
        - An empty TodoForm
        - Status columns for display grouping
        """
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm()
        context['status_columns'] = [
            ('PENDING', 'Pending'),
            ('IN_PROGRESS', 'In Progress'),
            ('DONE', 'Done'),
        ]
        return context
