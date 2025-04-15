from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import CustomAuthenticationForm
from .views import *

app_name = 'todo'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='todo/login.html',
                                     authentication_form=CustomAuthenticationForm),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='todo:login'), name='logout'),

    path('', TodoListView.as_view(), name='todo_list'),
    path('todo/create/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<uuid:pk>/update/', TodoUpdateView.as_view(),
         name='todo_update'),
    path('todo/<uuid:pk>/delete/', TodoDeleteView.as_view(),
         name='todo_delete'),
]
