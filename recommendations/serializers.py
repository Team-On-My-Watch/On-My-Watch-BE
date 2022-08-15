from rest_framework import serializers
from recommendations.models import User, Tag, Recommendation, Comment, Follow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


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
        fields = ('id', 'user', 'reason', 'saved_by', 'imdbid', 'title', 'medium', 'genre', 'tag', 'description', 'streaming_service', 'poster')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # recommendation = RecommendationSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'recommendation', 'comment', 'created_at')


# follow and unfollow feature
class FollowSerializer(serializers.ModelSerializer):
    following = serializers.ReadOnlyField(source='following.username')
    user_following = UserSerializer(source='following', read_only=True)

    class Meta:
        model = Follow
        fields = ('id', 'user_following', 'following')