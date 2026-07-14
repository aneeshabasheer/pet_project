from django.urls import path
from .views import *

urlpatterns = [
    path('',PetshopListView.as_view(),name='pet_list'),

    path('add/',PetshopCreateView.as_view(),name='pet_add'),

    path('edit/<int:pk>/',PetshopUpdateView.as_view(),name='pet_edit'),

    path('delete/<int:pk>/',PetshopDeleteView.as_view(),name='pet_delete'),

]