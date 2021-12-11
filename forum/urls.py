from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('thread/<int:thread_id>/', views.thread_view, name='thread'),
    path('delete_thread/<int:pk>/', views.DeleteThread.as_view(), name='delete_thread'),
    path('thread_form/', views.ThreadCreationView.as_view(), name='thread_form'),
]
