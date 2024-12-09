from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@test.ru", password="1234")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            place="Какое-либо место",
            time_action="18:05:00",
            action="Какое-либо действие",
            owner=self.user,
        )

    def test_habit_list(self):
        """Тестирование вывода списка привычек."""
        url = reverse("habits:habits-list")
        response = self.client.get(url)

        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.id,
                    "owner": self.user.pk,
                    "place": "Какое-либо место",
                    "time_action": "18:05:00",
                    "action": "Какое-либо действие",
                    "is_nice": self.habit.is_nice,
                    "related_habit": self.habit.related_habit,
                    "frequency": self.habit.frequency,
                    "remuneration": self.habit.remuneration,
                    "lead_time": self.habit.lead_time,
                    "is_published": self.habit.is_published,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data, result)

    def test_habit_retrieve(self):
        """Тестирование вывода одной привычки."""
        url = reverse("habits:habits-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        """Тестирование создания привычки."""
        url = reverse("habits:habits-create")

        data = {
            "owner": self.user.pk,
            "place": "Какое-либо место",
            "action": "Какое-либо действие",
            "time_action": "18:05:00",
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Тестирование обновления привычки."""
        url = reverse("habits:habits-update", args=(self.habit.pk,))
        data = {"place": "Обновлённое", "action": "Действие обновлено"}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            data,
            {
                "id": self.habit.id,
                "owner": self.user.pk,
                "place": "Обновлённое",
                "time_action": self.habit.time_action,
                "action": "Действие обновлено",
                "is_nice": self.habit.is_nice,
                "related_habit": self.habit.related_habit,
                "frequency": self.habit.frequency,
                "remuneration": self.habit.remuneration,
                "lead_time": self.habit.lead_time,
                "is_published": self.habit.is_published,
            },
        )

    def test_habit_delete(self):
        """Тестирование удаления привычки."""
        url = reverse("habits:habits-delete", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_lead_time(self):
        """Тестирование время на выполнение привычки."""
        url = reverse("habits:habits-create")
        data = {
            "owner": self.user.pk,
            "place": "Какое-либо место",
            "action": "Какое-либо действие",
            "lead_time": "121",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_frequency(self):
        """Тестирование периодичности привычки."""
        url = reverse("habits:habits-create")
        data = {
            "owner": self.user.pk,
            "place": "Какое-либо место",
            "action": "Какое-либо действие",
            "frequency": 0,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)