from django.urls import path
from . import views

app_name = 'user_api_integration'

urlpatterns = [
    path('user-api-integration/get-user/<int:id>/', views.get_user, name='get_user'),
    path('user-api-integration/create-user/', views.create_user, name='create_user'),
    path('user-api-integration/patch-user/<int:id>/', views.patch_user, name='patch_user'),
    path('user-api-integration/delete-user/<int:id>/', views.delete_user, name='delete_user'),
    path('user-api-integration/get-users/', views.get_users, name='get_users'),
    path('user-api-integration/create-users/', views.create_users, name='create_users'),
    path('user-api-integration/patch-users/', views.patch_users, name='patch_users'),
    path('user-api-integration/delete-users/', views.delete_users, name='delete_users'),
    path('user-api-integration/create-patch-delete/', views.create_patch_delete, name='create_patch_delete')
]