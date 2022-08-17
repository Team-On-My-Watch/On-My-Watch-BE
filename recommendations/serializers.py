from rest_framework import serializers
from recommendations.models import User, Tag, Recommendation, Comment, Follow


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()

    def get_followers(self, obj):
        follow_objects = Follow.objects.filter(followee=obj)
        followers = [follow_object.follower.username for follow_object in follow_objects]
        return followers

    class Meta:
        model = User
        fields = ('id', 'username', 'followers')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'tags')


class RecommendationSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    tag = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, slug_field="tags")
    saved_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")

    class Meta:
        model = Recommendation
        fields = ('id', 'user', 'reason', 'saved_by', 'imdbid', 'title', 'medium', 'genre', 'tag', 'description', 'streaming_service', 'poster', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'recommendation', 'comment', 'created_at')


class FollowingSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()

    def get_following(self, obj):
        follow_objects = Follow.objects.filter(follower=obj)
        following = [follow_object.followee.username for follow_object in follow_objects]
        return following

    class Meta:
        model = User
        fields = ('id', 'username', 'following')