import logging
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date
from bson import ObjectId

# Set up logging to debug command loading
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        # Simplify deletion logic to avoid dependency issues
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Create users with unique ObjectIds        

        # Explicitly create IDs for all objects using ObjectId
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]

        # Ensure all users are saved before referencing them in teams
        for user in users:
            user.save()

        # Create teams
        team1 = Team(id=ObjectId(), name='Blue Team')
        team2 = Team(id=ObjectId(), name='Gold Team')

        # Ensure teams are saved only after all users are saved and committed
        team1.save()
        team2.save()
        team1.members.add(*users[:3])
        team2.members.add(*users[3:])


        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], activity_type='Cycling', duration=60, date=date(2025, 4, 1)),
            Activity(id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120, date=date(2025, 4, 2)),
            Activity(id=ObjectId(), user=users[2], activity_type='Running', duration=90, date=date(2025, 4, 3)),
            Activity(id=ObjectId(), user=users[3], activity_type='Strength', duration=30, date=date(2025, 4, 4)),
            Activity(id=ObjectId(), user=users[4], activity_type='Swimming', duration=75, date=date(2025, 4, 5)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=team1, points=300),
            Leaderboard(id=ObjectId(), team=team2, points=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
            Workout(id=ObjectId(), name='Strength Training', description='Training for strength', duration=30),
            Workout(id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
        logger.debug("populate_db.py script loaded successfully.")
