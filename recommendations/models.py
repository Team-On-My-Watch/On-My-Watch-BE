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
    tags = models.TextField(max_length=50)


class Recommendation(BaseModel):
    TV_SHOW = 'TVS'
    MOVIE = 'M'
    STATUS_CHOICES = [
        (TV_SHOW, 'TV Show'), (MOVIE, 'Movie'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    reason = models.TextField(max_length=750)
    saved_by = models.ManyToManyField(User, related_name='saves', blank=True)
    imdbid = models.TextField(max_length=100)
    title = models.CharField(max_length=125)
    medium = models.CharField(max_length=3, choices=STATUS_CHOICES)
    genre = models.CharField(max_length=200)
    tag = models.ManyToManyField(Tag, related_name='user_tags')
    description = models.TextField(max_length=1000)
    streaming_service = models.CharField(max_length=50, null=True, blank=True)
    poster = models.ImageField(max_length=100, null=True)


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=750)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'], name='unique_following')
        ]



