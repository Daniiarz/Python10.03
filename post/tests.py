from django.test import TestCase

from users.models import CustomUser, UserProfile


def a_b(a, b) -> int:
    return a + b


class ABTestCase(TestCase):
    def test_a_b_returns_proper_value(self):
        a = 2
        b = 2
        result = a_b(a, b)
        self.assertEqual(result, a + b)


class BlogTestCase(TestCase):

    def setUp(self) -> None:
        self.user: CustomUser = CustomUser.objects.create_user(
            username="123",
            password="123",
        )

    def test_date_view(self):
        response = self.client.get("/blog/date/")

        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        data = {
            "bio": "Ya chelovek",
            "age": 15
        }

        profile = self.user.profile
        self.assertEqual(profile.age, None)
        self.assertEqual(profile.bio, None)

        self.client.force_login(self.user)
        response = self.client.post("/accounts/profile/", data=data)

        self.assertEqual(response.status_code, 200)
        profile.refresh_from_db()

        self.assertEqual(profile.age, data["age"])
        self.assertEqual(profile.bio, data["bio"])


