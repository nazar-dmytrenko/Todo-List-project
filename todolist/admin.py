from django.contrib import admin

from todolist.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "deadline", "is_done"]
    list_filter = ["content", "created_at"]
    search_fields = ["content", "tags__name"]


admin.site.register(Tag)