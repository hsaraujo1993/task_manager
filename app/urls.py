"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import login_view, register_view, logout_view
from tasks.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView
from tags.views import TagCreateView, TagLisTView, TagDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tasks/', TaskListView.as_view(), name='tasks_list'),
    path('new_task/', TaskCreateView.as_view(), name='new_task'),
    path('detail_task/<uuid:pk>/', TaskDetailView.as_view(), name='detail_task'),
    path('update_task/<uuid:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('delete_task/<uuid:pk>/', TaskDeleteView.as_view(), name='delete_task'),

    path('new_tag/', TagCreateView.as_view(), name='new_tag'),
    path('tags/', TagLisTView.as_view(), name='tags_list'),
    path('tags/<int:pk>/', TagDeleteView.as_view(), name='delete_tag'),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
