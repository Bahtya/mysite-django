from django.contrib import admin

from .models import Author, Blog, Tag

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorname','email')

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name','create_time')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('caption','author')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)
