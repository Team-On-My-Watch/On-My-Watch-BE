"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recommendations import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # User Authentication
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # Recommendation Views
    path('api/recommendation/', views.RecommendationAddListView.as_view()),
    path('api/recommendation/<int:pk>/', views.RecommendationDetailView.as_view()),
    path('api/recommendation/<int:pk>/comment/', views.CommentAddView.as_view()),
    path('api/recommendation/<int:pk>/delete/', views.RecommendationDestroyView.as_view()),
    # Follow Views
    path('api/follows/', views.FollowCreateView.as_view()),
    path('api/follows/<int:pk>/delete/', views.FollowRemoveView.as_view()),
    path('api/myfollowers/', views.FollowerView.as_view()),
    path('api/following/', views.FollowingView.as_view()),
    # Watch list
    path('api/user/watchlist/recommendations/', views.UserWatchListView.as_view()),
    path('api/recommendation/<int:pk>/watchlist/', views.AddWatchListCardView.as_view()),
    # Watched list
    path('api/watchedlist/', views.UserWatchedListView.as_view()),
    path('api/recommendation/<int:pk>/watchedlist', views.WatchedListView.as_view()),
    # Tags
    path('api/tags/', views.AddTagListView.as_view()),
    path('api/tag/<int:pk>/delete/', views.TagDestroyView.as_view()),
    # Users
    path('api/user/<int:pk>/recommendations/', views.UserRecommendationListView.as_view()),
    # Search
    path('api/search/movie/recommendations/', views.MovieSearchRecommendationView.as_view()),
    path('api/search/tvs/recommendations/', views.TVSSearchRecommendationView.as_view()),
    path('api/search/recommendations/', views.SearchRecommendationView.as_view()),
]
