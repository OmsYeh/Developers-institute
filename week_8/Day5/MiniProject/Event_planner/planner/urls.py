from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resourcecreation/', views.resource_creation, name='resource_creation'),
    path('viewlist/', views.list_view, name='list_view'),
    path('guests/', views.guest_list, name='guests'),
    path('location/', views.location_picker, name='location'),
    path('theme/', views.theme_picker, name='theme')
]
