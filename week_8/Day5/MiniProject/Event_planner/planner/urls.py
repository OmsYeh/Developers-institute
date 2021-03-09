from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('resourcecreation/', views.ResourceCreateView.as_view(), name='new-entry'),
    path('guests/', views.guest_list, name='guests'),
    path('location/', views.location_picker, name='location'),
    path('theme/', views.theme_picker, name='theme'),
    path('shoppingList/', views.list_view, name='list-creation'),
]
