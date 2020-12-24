from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('name', 'is_student', 'description', 'created', 'modified')
    list_filter = ('is_student', 'created', 'modified')

admin.site.register(Post, PostAdmin)
