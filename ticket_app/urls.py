from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('ticket_create/', views.ticket_create, name='ticket_create'),
    path('ticket_view/', views.ticket_view, name='ticket_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ticket_update/<int:pk>', views.ticket_update, name='ticket_update'),
    path('ticket_delete/<int:pk>', views.ticket_delete, name='ticket_delete')
]