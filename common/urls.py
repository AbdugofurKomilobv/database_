from django.urls import path

from .views import *


urlpatterns = [
    path('',EmployesView.as_view(),name='emp'),
    path('add/',FormAdd.as_view(),name='emp_add')

]