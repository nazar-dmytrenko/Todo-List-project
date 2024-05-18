"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from todolist.views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCompleteView,
    TaskUndoView,

    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/complete/", TaskCompleteView.as_view(), name="task-complete"),
    path("<int:pk>/undo/", TaskUndoView.as_view(), name="task-undo"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "todolist"
