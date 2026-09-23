from django.contrib import admin
from .models import CollabRequest, Comment, Like, Post, SavedPost 


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(SavedPost)
admin.site.register(CollabRequest)
