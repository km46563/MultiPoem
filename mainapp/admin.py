from django.contrib import admin

from .models import (
        Post,
        Comment,
        Follow,
        Like,
        SavedPost,
        Profile,
        CollabRequest,
        PostReport,
        UserReport,
        FeedSession,
        PostView
        )

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(SavedPost)
admin.site.register(Profile)
admin.site.register(CollabRequest)
admin.site.register(PostReport)
admin.site.register(UserReport)
admin.site.register(FeedSession)
admin.site.register(PostView)
