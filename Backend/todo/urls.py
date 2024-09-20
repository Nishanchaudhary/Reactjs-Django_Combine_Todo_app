from django.urls import path
from .views import list_todo, add_todo, update_todo, delete_todo

urlpatterns = [
    path('todos/', list_todo, name='list_todo'),            # GET: List all todos
    path('todos/add/', add_todo, name='add_todo'),          # POST: Add a new todo
    path('todos/<int:pk>/update/', update_todo, name='update_todo'),  # PUT: Update a specific todo
    path('todos/<int:pk>/delete/', delete_todo, name='delete_todo'),  # DELETE: Delete a specific todo
]
