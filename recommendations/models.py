from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f'<User username={self.username} pk={self.pk}>'

class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    tags = models.TextField(max_length=500)


class Recommendation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    reason = models.TextField(max_length=750)
    favorite = models.ManyToManyField(User, related_name='favorites', blank=True)
    imdbid = models.TextField(max_length=100)
    title = models.CharField(max_length=125)
    medium = models.CharField(max_length=50)
    genre = models.CharField(max_length=200)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='user_tags')
    description = models.TextField(max_length=1000)
    streaming_service = models.CharField(max_length=50, null=True, blank=True)
    poster = models.ImageField(max_length=100)


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=750)
