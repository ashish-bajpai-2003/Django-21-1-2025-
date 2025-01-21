from django.urls import path
from . import views

urlpatterns = [
    path('cre/' , views.create),
    path('ab/' , views.about),
    path('in/' , views.index),
]