from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        print('populate_db command loaded')
        # Create test users
        user1 = User.objects.create(email='user1@example.com', name='User One', password='password1')
        user2 = User.objects.create(email='user2@example.com', name='User Two', password='password2')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')

        # Add users to teams
        team1.members.add(user1)
        team2.members.add(user2)

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-10')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-10')

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=100)
        Leaderboard.objects.create(team=team2, score=150)

        # Create test workouts
        Workout.objects.create(name='Morning Run', description='A quick morning run', duration=30)
        Workout.objects.create(name='Evening Yoga', description='Relaxing yoga session', duration=60)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
