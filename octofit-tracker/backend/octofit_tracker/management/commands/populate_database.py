import logging

# Set up logging to debug command loading
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("populate_database.py script loaded successfully.")

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Explicitly drop collections to ensure no residual data remains
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.filter(id__isnull=False).delete()

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        for user in users:
            user.save()

        # Create teams
        team1 = Team(name='Blue Team')
        team1.members.add(users[0], users[1], users[2])
        team1.save()

        team2 = Team(name='Gold Team')
        team2.members.add(users[3], users[4])
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=users[1], activity_type='Crossfit', duration=120, date='2025-04-02'),
            Activity(user=users[2], activity_type='Running', duration=90, date='2025-04-03'),
            Activity(user=users[3], activity_type='Strength', duration=30, date='2025-04-04'),
            Activity(user=users[4], activity_type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, points=300),
            Leaderboard(team=team2, points=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))