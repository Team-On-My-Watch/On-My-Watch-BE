from rest_framework import serializers
from recommendations.models import User, Tag, Recommendation, Comment, Follow


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'image',)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'tags')


class RecommendationSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    tag = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, slug_field="tags")
    saved_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")
    user_info = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Recommendation
        fields = ('id', 'user', 'user_info', 'reason', 'saved_by', 'imdbid', 'title', 'medium', 'genre', 'tag', 'description', 'streaming_service', 'poster', 'created_at', 'related_shows', 'keywords', 'actors', 'emotion')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'recommendation', 'comment', 'created_at')


class FollowSerializer(serializers.ModelSerializer):
    follower  = serializers.SlugRelatedField(slug_field="username", read_only=True)
    
    class Meta:
        model = Follow
        fields= ('follower',)


class FollowingSerializer(serializers.ModelSerializer):
    followee = serializers.SlugRelatedField(slug_field="username", read_only=True)
    followee_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Follow
        fields= ('id','followee', 'followee_id',)


class FollowUnfollowSerializer(serializers.ModelSerializer):
    followee = serializers.PrimaryKeyRelatedField(read_only=True)
    follower = serializers.PrimaryKeyRelatedField(read_only=True)
    followee_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Follow
        fields = ( 'pk','follower', 'followee', 'followee_name',)

