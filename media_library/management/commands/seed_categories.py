from django.core.management.base import BaseCommand
from django.utils.text import slugify
from media_library.models import Category

class Command(BaseCommand):
    help = "Create the default MediaHub categories"

    def handle(self, *args, **options):
        defaults = {
            "Education": "Lessons, tutorials and explainers.",
            "Entertainment": "Films, performances and creative media.",
            "Music & Audio": "Podcasts, music and recorded discussions.",
            "Photography": "Photography, illustrations and visual stories.",
            "Technology": "Technology talks, demos and product walkthroughs.",
        }
        for name, description in defaults.items():
            Category.objects.get_or_create(
                slug=slugify(name),
                defaults={"name": name, "description": description},
            )
        self.stdout.write(self.style.SUCCESS("Default categories are ready."))
