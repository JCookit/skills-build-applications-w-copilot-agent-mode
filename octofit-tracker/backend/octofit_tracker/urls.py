from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TestEndpoint

router = DefaultRouter()
# Add `basename` arguments to the viewset registrations
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activity', views.ActivityViewSet, basename='activity')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', include(router.urls)),
    path('api-root/', include(router.urls)),
    path('test-endpoint', TestEndpoint.as_view(), name='test-endpoint'),
]
