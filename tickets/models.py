from django.db import models


class Ticket(models.Model):
    class Priority(models.TextChoices):
        LOW = "low", "Төмен"
        MEDIUM = "medium", "Орташа"
        HIGH = "high", "Жоғары"

    class Status(models.TextChoices):
        NEW = "new", "Жаңа"
        IN_PROGRESS = "in_progress", "Орындалуда"
        DONE = "done", "Дайын"

    title = models.CharField("Тақырып", max_length=200)
    description = models.TextField("Сипаттама")
    priority = models.CharField(
        "Басымдық",
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    status = models.CharField(
        "Мәртебе",
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    created_at = models.DateTimeField("Құрылған уақыты", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"#{self.pk} {self.title}"
