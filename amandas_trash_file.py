# class UserSerializer(serializers.ModelSerializer):
#     # followers = serializers.SerializerMethodField()

#     # def get_followers(self, obj):
#     #     follow_objects = Follow.objects.filter(followee=obj)
#     #     followers = [follow_object.follower.username for follow_object in follow_objects]
#     #     return followers

#     class Meta:
#         model = User
#         fields = ('id', 'username',)
#         #removed 'followers from fields


# class FollowingSerializer(serializers.ModelSerializer):
#     following = serializers.SerializerMethodField()

#     def get_following(self, obj):
#         follow_objects = Follow.objects.filter(follower=obj)
#         following = [follow_object.followee.username for follow_object in follow_objects]
#         return following

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'following')


# # get list of followers
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer 


# # get list of users you are following
# class UserFollowingDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = FollowingSerializer 


# path('api/user/<int:pk>/followers/', views.UserDetailView.as_view()),
# path('api/user/<int:pk>/following/', views.UserFollowingDetailView.as_view()),