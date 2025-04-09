from django.http import JsonResponse
from django.views import View
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class TestEndpoint(View):
    def get(self, request):
        return JsonResponse({"message": "API is working on https://laughing-waffle-jrr7p557gxr2p6jx-8000.app.github.dev and localhost:8000"})

# Placeholder implementations for the viewsets
class UserViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "List of users"})

class TeamViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "List of teams"})

class ActivityViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "List of activities"})

class LeaderboardViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "Leaderboard data"})

class WorkoutViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "List of workouts"})
