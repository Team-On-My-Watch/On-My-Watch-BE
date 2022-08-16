from django.contrib import admin
from .models import User, Tag, Recommendation, Comment, Follow


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Recommendation)
admin.site.register(Comment)
admin.site.register(Follow)
