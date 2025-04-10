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
        activity1 = Activity.objects.create(name='Running', description='Morning run in the park', duration=30, user=user1)
        activity2 = Activity.objects.create(name='Cycling', description='Evening cycling session', duration=45, user=user2)

        # Create test leaderboards
        leaderboard1 = Leaderboard.objects.create(name='Weekly Challenge')
        leaderboard1.activities.add(activity1, activity2)

        # Create test workouts
        workout1 = Workout.objects.create(name='Cardio Blast', description='High-intensity cardio workout', duration=60)
        workout2 = Workout.objects.create(name='Strength Training', description='Full-body strength training', duration=50)

        # Print success message
        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
