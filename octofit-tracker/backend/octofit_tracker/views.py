from django.http import JsonResponse
from django.views import View
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class TestEndpoint(View):
    def get(self, request):
        return JsonResponse({"message": "API is working on https://laughing-waffle-jrr7p557gxr2p6jx-8000.app.github.dev and localhost:8000"})

# Update viewsets to return data from the database
class UserViewSet(ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# Update TeamViewSet to fetch members manually
class TeamViewSet(ViewSet):
    def list(self, request):
        teams = Team.objects.all()
        team_data = []
        for team in teams:
            team_dict = {
                "id": str(team.id),
                "name": team.name,
                "members": [
                    {
                        "id": str(member.id),
                        "email": member.email,
                        "name": member.name,
                        "age": member.age,
                        "created_at": member.created_at
                    }
                    for member in team.members.all()
                ]
            }
            team_data.append(team_dict)
        return Response(team_data)

class ActivityViewSet(ViewSet):
    def list(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

class LeaderboardViewSet(ViewSet):
    def list(self, request):
        leaderboard = Leaderboard.objects.all()
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)

class WorkoutViewSet(ViewSet):
    def list(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
