from django.urls import path, include
from .views import *


app_name = 'hrapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('training_programs/', training_program_list, name='training_program'),
    path('departments/', department_list, name='departments'),
    path('departments/<int:department_id>/', department_details, name='department'),
    path('computers/', computer_list, name='computers'),
    path('employees/form', employee_form, name='employee_form'),
]
