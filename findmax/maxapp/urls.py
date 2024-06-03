from django.urls import path
from.import views

urlpatterns = [
    path('',views.find_max,name='find_max'),
]
