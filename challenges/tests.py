from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Challenge, ChallengeParticipation

class ChallengesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.challenge = Challenge.objects.create(
            title='Test Challenge',
            description='Test Description',
            start_date='2025-01-01'
        )

    def test_challenges_list_loads(self):
        response = self.client.get(reverse('challenges_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Challenge')

    def test_challenge_detail_loads(self):
        response = self.client.get(reverse('challenge_detail', args=[self.challenge.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Description')

    def test_join_and_complete_challenge(self):
        self.client.login(username='testuser', password='testpassword123')
        
        # User joins the challenge
        response = self.client.post(reverse('join_challenge', args=[self.challenge.id]))
        self.assertRedirects(response, reverse('challenge_detail', args=[self.challenge.id]))
        
        # Check participation is created
        participation = ChallengeParticipation.objects.get(user=self.user, challenge=self.challenge)
        self.assertFalse(participation.is_completed)
        self.assertEqual(self.challenge.participants.count(), 1)
        
        # User completes the challenge
        dummy_image = SimpleUploadedFile("test_proof.jpg", b"file_content", content_type="image/jpeg")
        complete_res = self.client.post(reverse('complete_challenge', args=[self.challenge.id]), {'proof_image': dummy_image})
        self.assertRedirects(complete_res, reverse('challenge_detail', args=[self.challenge.id]))
        
        # Check completion status updated
        participation.refresh_from_db()
        self.assertTrue(participation.is_completed)
