from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

# Fix redundant `source='id'` in ActivitySerializer
class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(source='user.id', read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'

# Fix redundant `source='id'` in LeaderboardSerializer
class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    team = serializers.CharField(source='team.id', read_only=True)

    class Meta:
        model = Leaderboard
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
