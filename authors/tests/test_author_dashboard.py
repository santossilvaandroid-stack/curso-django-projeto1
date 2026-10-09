from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthorDashboardTest(TestCase):
    def test_dashboard_redirects_anonymous_users_to_login(self):
        response = self.client.get(reverse('authors:dashboard'))

        self.assertRedirects(
            response,
            f"{reverse('authors:login')}?next={reverse('authors:dashboard')}",
        )

    def test_authenticated_user_can_view_dashboard(self):
        user = User.objects.create_user(username='my_user', password='my_pass')
        self.client.force_login(user)

        response = self.client.get(reverse('authors:dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authors/pages/dashboard.html')
        self.assertContains(response, user.username)
