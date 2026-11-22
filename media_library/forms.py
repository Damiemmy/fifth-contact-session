from django import forms
from .models import MediaItem

class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ["title", "description", "media_type", "category", "file", "cover_image", "creator"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Give your media a clear title"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "What should viewers know about this upload?"}),
            "creator": forms.TextInput(attrs={"placeholder": "Your name or organisation"}),
        }

    def clean_file(self):
        uploaded = self.cleaned_data.get("file")
        if uploaded and uploaded.size > 100 * 1024 * 1024:
            raise forms.ValidationError("File size must not exceed 100 MB.")
        return uploaded
