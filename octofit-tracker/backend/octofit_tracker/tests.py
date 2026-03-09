from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Pushups', description='Do pushups')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30, date=timezone.now().date())
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, week=timezone.now().date())

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.team, self.team)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
