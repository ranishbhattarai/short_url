from django.db import models
from django.conf import settings
from slinks.utils import generate_secure_short_key

# Create your models here.

# Model to store short links
class ShortLink(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    original_url = models.URLField(max_length=2048)
    short_key = models.CharField(max_length=6, unique=True , blank=True)
    expires_at = models.DateField(null=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.short_key
    
    # Overriding save method to generate short_key upon creation
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new and not self.short_key:
            self.short_key = generate_secure_short_key(length=6)
            super().save(*args, **kwargs)

