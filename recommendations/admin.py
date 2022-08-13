from django.contrib import admin
from .models import User, Tag, Recommendation, Comment


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Recommendation)
admin.site.register(Comment)
