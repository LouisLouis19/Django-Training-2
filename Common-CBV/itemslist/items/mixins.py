from django.utils import timezone

class TimestampMixin:
    """
    A mixin to automatically update created_at and updated_at fields.
    """
    def save(self, *args, **kwargs):
        now = timezone.now()

        if not self.pk:
            self.created_at = now
        self.updated_at = now

        super().save(*args, **kwargs)
