from django.urls import path
from .views import *

urlpatterns = [
    path('send-feedback/', SendCreateFeedbackAPIVIew.as_view(), name='feedback')
]
