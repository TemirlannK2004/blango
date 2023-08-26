from django.contrib import admin
from django.contrib import admin
from blog.models import Tag, Post


# Register your models here.
@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ['value']