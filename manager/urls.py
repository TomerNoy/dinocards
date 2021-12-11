from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.edit, name='edit'),
    path('remove_user/', views.remove_user, name='remove_user'),
    path('create_card/', views.CreateCardView.as_view(), name='create_card'),
    path('delete_card/', views.delete_card, name='delete_card'),
]
