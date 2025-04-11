from djongo import models
from djongo.models import ObjectIdField

# Ensure `_id` is auto-generated by MongoDB and does not require a default value
class User(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "users"

class Team(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    members = models.JSONField(default=list)  # Default to an empty list

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teams"

class Activity(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.name}"

    class Meta:
        db_table = "activity"

class Leaderboard(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

    class Meta:
        db_table = "leaderboard"

class Workout(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name

    class Meta:
        db_table = "workouts"
