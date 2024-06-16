from django.contrib import admin

from todolist.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "datetime", "deadline", "is_completed"]
    list_filter = ["content", "datetime"]
    search_fields = ["content", "tags__name"]


admin.site.register(Tag)
