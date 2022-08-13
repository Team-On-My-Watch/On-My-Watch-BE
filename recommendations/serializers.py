from rest_framework import serializers
from recommendations.models import User, Tag, Recommendation, Comment


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
    favorited_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")

    class Meta:
        model = Recommendation
        fields = ('id', 'user', 'reason', 'favorited_by', 'imdbid', 'title', 'medium', 'genre', 'tag', 'description', 'streaming_service', 'poster')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'user', 'recommendation', 'comment')
