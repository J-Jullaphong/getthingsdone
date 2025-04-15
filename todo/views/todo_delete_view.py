from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseForbidden
from django.views import View

from ..models import Todo


class TodoDeleteView(LoginRequiredMixin, View):
    """
    This view is for deleting a todo item.
    It accepts AJAX POST requests and ensures that only the item's owner can delete it.
    """

    def post(self, request, pk):
        """
        This method handles the AJAX POST request to delete the specified todo item.
        If the item doesn't exist or isn't owned by the user, it returns HTTP 403.
        """
        try:
            todo = Todo.objects.get(pk=pk, user=request.user)
            todo.delete()
            return JsonResponse({'message': 'Deleted'})
        except Todo.DoesNotExist:
            return HttpResponseForbidden()
