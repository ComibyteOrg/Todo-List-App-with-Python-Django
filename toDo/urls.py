from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homeView.as_view(), name='home'), 
    path('add_task', views.addTask.as_view(), name='add_task'),
    path('delete/<int:task_id>/', views.delete_task.as_view(), name='delete_task'),
    path('update/<int:task_id>/', views.update_task.as_view(), name='update_task'),
    path('register/', views.registerView.as_view(), name="register"), 
    path('login/', views.loginView.as_view(), name="login"), 
    path('logout/', views.logoutView.as_view(), name="logout"),
]
