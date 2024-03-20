from django.urls import path
from .views import create_reminder, list_reminders

urlpatterns = [
    path('api/reminders/', create_reminder, name='create_reminder'),
	path('api/reminders/list/', list_reminders, name='list_reminders'),
]
