from .views import taxi_page_view
from django.urls import path

urlpatterns = [
    path('', taxi_page_view, name='taxi'),
]
