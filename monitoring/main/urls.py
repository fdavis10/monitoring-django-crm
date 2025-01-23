from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('incedents-api/', views.incedents_, name='api'),
    path('incedent-template/', views.incedent_template, name='page'),
]
