from django.contrib import admin
from .models import Lesson, Topic

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')
    ordering = ('id',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_id', 'name', 'lesson', 'picture', 'description')
    search_fields = ('name', 'description')
    list_filter = ('lesson',)
    ordering = ('topic_id',)
