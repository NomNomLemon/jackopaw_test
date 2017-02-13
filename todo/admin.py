from django.contrib import admin
from .models import Task, Log


class LogsInline(admin.TabularInline):
    model = Log
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'status', 'created_at', 'updated_at')
    inlines = [LogsInline]


admin.site.register(Task, TaskAdmin)
