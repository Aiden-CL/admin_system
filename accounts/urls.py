from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('logout/', views.AdminLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('users/', views.user_list_view, name='user_list'),
    path('users/create/', views.user_create_view, name='user_create'),
    path('users/<int:pk>/edit/', views.user_update_view, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete_view, name='user_delete'),
    path('logs/', views.operation_log_view, name='operation_log'),
]
