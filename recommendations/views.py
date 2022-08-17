from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from recommendations.permissions import IsOwner
from recommendations.models import Recommendation, Comment, Follow, User, Tag
from .serializers import CommentSerializer, RecommendationSerializer, TagSerializer, UserSerializer

# view Recommendations/ add Recommendations
class RecommendationAddListView(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Recommendation detail
class RecommendationDetailView(generics.RetrieveAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


# delete Recommendation
class RecommendationDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [IsOwner]


# get recommendation and post comment
class CommentAddView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(recommendation_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        recommendation = get_object_or_404(Recommendation, pk=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, recommendation=recommendation)


# get list of followers
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 


class AddWatchListCardView(APIView):

    def post(self, request, **kwargs):
        user = self.request.user
        recommendation = get_object_or_404(Recommendation, pk=self.kwargs['pk'])
        user.saves.add(recommendation)
        serializer = RecommendationSerializer(recommendation, context={'request': request})
        return Response(serializer.data, status=201)

    def delete(self, request, **kwargs):
        user = self.request.user
        recommendation = get_object_or_404(Recommendation, pk=self.kwargs['pk'])
        user.saves.remove(recommendation)
        serializer = RecommendationSerializer(recommendation, context={'request': request})
        return Response(serializer.data, status=204)


class UserWatchListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        return self.request.user.saves.all()


# add tags/view all tags
class AddTagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# delete tags
class TagDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# All user recommendations
class UserRecommendationListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        return Recommendation.objects.filter(user_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs.get("pk"))
        serializer.save(user=user)
