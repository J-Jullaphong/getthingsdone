from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import CreateView

from ..forms import TodoForm
from ..models import Todo


class TodoCreateView(LoginRequiredMixin, CreateView):
    """
    This view is for creating new todo items.
    It accepts AJAX POST requests, validates the form, and returns JSON responses.
    """
    model = Todo
    form_class = TodoForm

    def post(self, request, *args, **kwargs):
        """
        This method handles POST requests to create a todo item.
        It attaches the logged-in user to the form instance and returns a JSON response.
        """
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return JsonResponse({'message': 'Created'}, status=200)
        return JsonResponse({'errors': form.errors}, status=400)
