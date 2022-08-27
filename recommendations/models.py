from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_photos', blank=True, null=True)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    reason = models.TextField(max_length=2500)
    saved_by = models.ManyToManyField(User, related_name='saves', blank=True)
    imdbid = models.TextField(max_length=100)
    title = models.CharField(max_length=125)
    medium = models.CharField(max_length=255)
    genre = models.JSONField(max_length=200, null=True)
    tag = models.ManyToManyField(Tag, related_name='user_tags')
    description = models.TextField(max_length=1000)
    streaming_service = models.JSONField(max_length=200, null=True)
    poster = models.TextField(max_length=500, null=True)
    related_shows = models.JSONField(max_length=200, null=True)
    keywords = models.JSONField(max_length=200, null=True)
    actors = models.JSONField(max_length=200, null=True)
    emotion = models.JSONField(max_length=400, null=True)
    watched_by = models.ManyToManyField(User, related_name="watches")


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=750)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows_user_initiated', null=True)
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows_user_received', null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'followee'], name='follower-followed')
        ]

    def __str__(self):
        return f'{self.follower} follows {self.followee}'
