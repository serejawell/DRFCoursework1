from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)  # Пользователь не должен изменять эти поля

    def validate(self, data):
        # Дополнительная валидация
        if data.get('reward') and data.get('linked_habit'):
            raise serializers.ValidationError(
                "Привычка не может одновременно иметь вознаграждение и связанную привычку.")

        if data.get('is_pleasant') and (data.get('reward') or data.get('linked_habit')):
            raise serializers.ValidationError("Приятная привычка не может иметь вознаграждения или связанные привычки.")

        if data.get('time_to_complete') and data['time_to_complete'] > 120:
            raise serializers.ValidationError("Время выполнения не может превышать 120 секунд.")

        if data.get('periodicity') and data['periodicity'] < 1:
            raise serializers.ValidationError("Периодичность выполнения должна быть не реже, чем раз в 7 дней.")

        if data.get('linked_habit') and not data['linked_habit'].is_pleasant:
            raise serializers.ValidationError("Связанной привычкой может быть только приятная привычка.")

        return data
