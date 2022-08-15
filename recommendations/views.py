from django.shortcuts import get_object_or_404
from rest_framework import generics
from recommendations.models import Recommendation, Comment, Follow, User
from .serializers import CommentSerializer, FollowSerializer, RecommendationSerializer


class RecommendationAddListView(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# get recommendation and post comment
class CommentAddView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(recommendation_id=self.kwargs["pk"].order_by('-created_at'))

    def perform_create(self, serializer):
        recommendation = get_object_or_404(Recommendation, pk=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, recommendation=recommendation)


# allows for unique follow object/relationship
class FollowUserView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        user_following = User.objects.get(username=self.request.data['following'])
        if user_following.id is not self.request.user.id:
            serializer.save(user=self.request.user.username, following=user_following.username)
        else:
            return 


