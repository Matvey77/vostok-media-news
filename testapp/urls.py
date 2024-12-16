from django.urls import path

from testapp.views import *


urlpatterns = [
    path('', test),
    path('rubric/<int:pk>', get_rubric, name='rubric')
]
