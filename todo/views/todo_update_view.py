from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from ..forms import TodoForm
from ..models import Todo


class TodoUpdateView(LoginRequiredMixin, View):
    """
    This view is for updating a todo item.
    It handles both full updates via modal form (GET + POST) and AJAX-only status updates (POST).
    """

    def get(self, request, pk):
        """
        This method returns the todo update form pre-filled with the current data.
        It is triggered via a Bootstrap modal.
        """
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        form = TodoForm(instance=todo)
        return render(request, 'todo/partials/update_todo_modal.html',
                      {'form': form, 'todo': todo})

    def post(self, request, pk):
        """
        This method handles two types of POST requests.
        1. If only 'status' is submitted, it updates the status of the todo item (used for drag-and-drop).
        2. Otherwise, it treats the request as a full form submission and updates all fields.
        """
        todo = get_object_or_404(Todo, pk=pk, user=request.user)

        if 'status' in request.POST and len(request.POST) == 2:
            todo.status = request.POST['status']
            todo.save()
            return JsonResponse(
                {'success': True, 'is_overdue': todo.is_overdue})

        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'errors': form.errors}, status=400)
