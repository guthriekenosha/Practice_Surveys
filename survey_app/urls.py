from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create),
    path('survey_dash', views.dashboard)
]
