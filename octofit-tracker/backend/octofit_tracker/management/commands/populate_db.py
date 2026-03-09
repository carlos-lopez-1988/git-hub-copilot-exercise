from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes')
        workout2 = Workout.objects.create(name='Flight Training', description='Aerial maneuvers')
        workout1.suggested_for.set(users)
        workout2.suggested_for.set(users)

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Web Swinging', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Suit Up', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Lasso Practice', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Detective Work', duration=90, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=200, week=timezone.now().date())
        Leaderboard.objects.create(team=dc, total_points=180, week=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
