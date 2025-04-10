from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

# Add verbose output to track progress
class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        self.stdout.write('Creating users...')
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Elliot Alderson', age=28),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Dade Murphy', age=25),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', age=29),
        ]
        User.objects.bulk_create(users)

        # Create teams
        self.stdout.write('Creating teams...')
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        blue_team.save()
        blue_team.members.set([users[0], users[1]])

        gold_team = Team(_id=ObjectId(), name='Gold Team')
        gold_team.save()
        gold_team.members.set([users[2], users[3], users[4]])

        # Create activities
        self.stdout.write('Creating activities...')
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60, date='2025-04-01'),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120, date='2025-04-02'),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=90, date='2025-04-03'),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=30, date='2025-04-04'),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=blue_team, points=300),
            Leaderboard(_id=ObjectId(), team=gold_team, points=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength', duration=30),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
