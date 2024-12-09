from rest_framework.serializers import ValidationError


class ExcludeValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        remuneration = dict(value).get(self.field2)
        if related_habit and remuneration:
            raise ValidationError(
                "В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. \
                Можно заполнить только одно из двух полей."
            )


class LeadTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)
        if duration and duration > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class RelatedNiceValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        is_nice = dict(value).get(self.field2)
        if related_habit and not is_nice:
            raise ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )


class NiceValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        is_nice = dict(value).get(self.field1)
        related_habit = dict(value).get(self.field2)
        remuneration = dict(value).get(self.field3)
        if is_nice and remuneration and related_habit:
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )


class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        frequency = dict(value).get(self.field)
        if isinstance(frequency, int) and (frequency > 7 or frequency < 1):
            raise ValidationError(
                "Периодичность привычки не может быть больше 7 и меньше 1."
            )