from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

# Explicitly handle `_id` field in serializers
class UserSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'email', 'name', 'age', 'created_at']

class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    members = serializers.ListField(child=serializers.CharField(), read_only=True)

    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    user = serializers.CharField(source='user._id', read_only=True)

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'duration', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    team = serializers.CharField(source='team._id', read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)

    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'duration']
