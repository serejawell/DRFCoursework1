from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (
    ExcludeValidator,
    LeadTimeValidator,
    RelatedNiceValidator,
    NiceValidator,
    FrequencyValidator,
)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            ExcludeValidator(field1="related_habit", field2="remuneration"),
            LeadTimeValidator(field="lead_time"),
            RelatedNiceValidator(field1="related_habit", field2="is_nice"),
            NiceValidator(
                field1="is_nice", field2="related_habit", field3="remuneration"
            ),
            FrequencyValidator(field="frequency"),
        ]