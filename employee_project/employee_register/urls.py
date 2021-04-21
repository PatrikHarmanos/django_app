from django.urls import path, include
from . import views

urlpatterns = [
    # GET and POST for insert operation
    path('', views.employee_form, name="employee_insert"),
    # GET and POST for update
    path('<int:id>/', views.employee_form, name="employee_update"),
    # delete
    path('delete/<int:id>/', views.employee_delete, name="employee_delete"),
    # retrive and display data
    path('list/', views.employee_list, name="employee_list")
]
