from pathlib import Path
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True)
    description = models.CharField(max_length=220, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class MediaItem(models.Model):
    class MediaType(models.TextChoices):
        VIDEO = "video", "Video"
        AUDIO = "audio", "Audio"
        IMAGE = "image", "Image"

    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=10, choices=MediaType.choices)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="items")
    file = models.FileField(
        upload_to="library/%Y/%m/",
        validators=[FileExtensionValidator(
            allowed_extensions=["mp4", "webm", "mov", "mp3", "wav", "ogg", "m4a", "jpg", "jpeg", "png", "gif", "webp"]
        )],
    )
    cover_image = models.ImageField(upload_to="covers/%Y/%m/", blank=True, null=True)
    creator = models.CharField(max_length=100, blank=True, default="MediaHub Creator")
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("media_detail", kwargs={"pk": self.pk})

    @property
    def file_extension(self):
        return Path(self.file.name).suffix.lower().lstrip(".")
