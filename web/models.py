from django.db import models
from django.utils.text import slugify
import uuid

class Flanes(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField(default='https://eurelec.pt/img/noimage.jpg')
    slug = models.SlugField(unique=True, blank=True)
    is_private = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.description = self.description.capitalize()
        if not self.slug:
            self.slug = slugify(self.name)
            while Flanes.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{str(uuid.uuid4())[:8]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
