from django.urls import path
from . import views

urlpatterns = [
      # ✅ Login & Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update/<int:pk>/', views.updateTask, name='update'),
    path('delete/<int:pk>/', views.deleteTask, name='delete'),
    path('', views.task_list, name='list'),
    path('register/', views.register_view, name='register'),

]
