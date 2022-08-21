from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from recommendations import permissions
import recommendations
from recommendations.permissions import IsOwner
from recommendations.models import Recommendation, Comment, User, Tag, Follow
from .serializers import CommentSerializer, RecommendationSerializer, TagSerializer, FollowSerializer, FollowingSerializer, FollowUnfollowSerializer


# --------------------------------------------RECOMMENDATIONS-------------------------------------
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


# -----------------------------------------------COMMENTS------------------------------------------
# get recommendation and post comment
class CommentAddView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(recommendation_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        recommendation = get_object_or_404(Recommendation, pk=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, recommendation=recommendation)


# -----------------------------------------------FOLLOWERS------------------------------------------
#list of followers
class FollowerView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.follows_user_received.all()


#list of users you are following
class FollowingView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.follows_user_initiated.all()


#follow a user
class FollowCreateView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowUnfollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # establishes variable for filtered queryset
        unique_query = self.queryset.filter(followee_id=self.request.data['followee'], follower_id=self.request.user)
        # conditional for if the unique query does not exist
        if len(unique_query) == 0:
            # when a Follow object is saved,the user is set as the user that made the request
            serializer.save(follower=self.request.user, followee_id=self.request.data['followee'])
            return
        else:
            return Response({"message": "You already follow this user."})


#unfollow
class FollowRemoveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowUnfollowSerializer
    permission_classes = [IsAuthenticated]


# -----------------------------------------------WATCH LIST------------------------------------------
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


# -----------------------------------------------WATCHED LIST------------------------------------------
class WatchedListView(APIView):

    def post(self, request, **kwargs):
        user = self.request.user
        recommendation = get_object_or_404(Recommendation, pk = self.kwargs['pk'])
        user.saves.add(recommendation)
        serializer = RecommendationSerializer(recommendation, context={'request': request})
        return Response(serializer.data, status=201)

    def delete(self, request, **kwargs):
        user = self.request.user
        recommendation = get_object_or_404(Recommendation, pk=self.kwargs['pk'])
        user.saves.remove(recommendation)
        serializer = RecommendationSerializer(recommendation, context={'request': request})
        return Response(serializer.data, status=204)


class UserWatchedListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        return self.request.user.saves.all()


# --------------------------------------------------TAGS------------------------------------------
# add tags/view all tags
class AddTagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# delete tags
class TagDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# --------------------------------------------------USERS------------------------------------------

# All user recommendations
class UserRecommendationListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        return Recommendation.objects.filter(user_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs.get("pk"))
        serializer.save(user=user)
