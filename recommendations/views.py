from http.client import HTTPResponse
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from recommendations import permissions
from rest_framework import filters
from recommendations.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from recommendations.models import Recommendation, Comment, User, Tag, Follow
from .serializers import CommentSerializer, RecommendationSerializer, TagSerializer, FollowSerializer, FollowingSerializer, FollowUnfollowSerializer, UserSerializer


# --------------------------------------------RECOMMENDATIONS---------------------------------------
# View Recommendations GET/ Add Recommendations POST
class RecommendationAddListView(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    filter_backends = [filters.SearchFilter]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Recommendation detail GET
class RecommendationDetailView(generics.RetrieveAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


# Delete Recommendation DELETE 
class RecommendationDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [IsOwner]


# -----------------------------------------------COMMENTS------------------------------------------
# View comments GET / Add comment POST
class CommentAddView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(recommendation_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        recommendation = get_object_or_404(Recommendation, pk=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, recommendation=recommendation)


# -----------------------------------------------FOLLOWERS------------------------------------------
# List of followers GET
class FollowerView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.follows_user_received.all()


# List of users you are following GET
class FollowingView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.follows_user_initiated.all()


# Follow a user POST
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


# Unfollow a user DELETE
class FollowRemoveView(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowUnfollowSerializer
    permission_classes = [IsAuthenticated]
    
# -----------------------------------------------WATCH LIST------------------------------------------
# Add show/movie to watch list POST / Remove show/movie from watch list DELETE
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


# View users watch list GET
class UserWatchListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        return self.request.user.saves.all()


# -----------------------------------------------WATCHED LIST------------------------------------------
# Add show/movie to watched list POST / Remove show/movie from watched list DELETE
class WatchedListView(APIView):

    def post(self, request, **kwargs):
        user = self.request.user
        recommendation = get_object_or_404(Recommendation, pk = self.kwargs['pk'])
        user.watches.add(recommendation)
        serializer = RecommendationSerializer(recommendation, context={'request': request})
        return Response(serializer.data, status=201)

    def delete(self, request, **kwargs):
        user = self.request.user
        recommendation = get_object_or_404(Recommendation, pk=self.kwargs['pk'])
        user.watches.remove(recommendation)
        serializer = RecommendationSerializer(recommendation, context={'request': request})
        return Response(serializer.data, status=204)


# View users watched list GET
class UserWatchedListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        return self.request.user.watches.all()


# --------------------------------------------------TAGS------------------------------------------
# Add tags POST / View all tags GET
class AddTagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Delete tags DELETE
class TagDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# --------------------------------------------------USERS------------------------------------------
# View all users recommendations GET 
class UserRecommendationListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        return Recommendation.objects.filter(user_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs.get("pk"))
        serializer.save(user=user)


# Search Recommendation
class SearchRecommendationView(generics.ListAPIView):
    serializer_class = RecommendationSerializer
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = Recommendation.objects.all()
        tag = self.request.query_params.get('tag')
        medium = self.request.query_params.get('medium')
        user = self.request.query_params.get('user')
        if medium is not None:
            queryset = queryset.filter(medium=medium)
        if tag is not None:
            queryset = queryset.filter(tag=tag)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

    search_fields = ['$title', '$description', 'imdbid', '$keywords', '$genre', '$streaming_service', '$reason']

# ---------------------------------------PROFILE IMAGE UPLOAD-----------------------------------------
# Add image for user avatar PATCH
class ImageView(APIView):
    parser_classes = [FileUploadParser]

    def patch(self, request, format=None):
        file = request.data['file']
        request.user.image.save(file.name, file, save=True)
        serialized_user = UserSerializer(request.user)
        return Response(serialized_user.data, status=206)
