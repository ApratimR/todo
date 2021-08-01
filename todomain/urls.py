from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_request),
    path('insert/',views.insert),
    path('delete/<int:todo_id>',views.delete),
    path('update/<int:todo_id>',views.update)
]