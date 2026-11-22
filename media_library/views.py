from django.db.models import Q, F
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Category, MediaItem
from .forms import MediaItemForm

def home(request):
    items = MediaItem.objects.select_related("category")[:8]
    context = {
        "featured_items": items[:3],
        "latest_items": items,
        "categories": Category.objects.all(),
        "total_items": MediaItem.objects.count(),
    }
    return render(request, "media_library/home.html", context)

def library(request):
    items = MediaItem.objects.select_related("category")
    query = request.GET.get("q", "").strip()
    media_type = request.GET.get("type", "")
    category = request.GET.get("category", "")
    if query:
        items = items.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(creator__icontains=query))
    if media_type in dict(MediaItem.MediaType.choices):
        items = items.filter(media_type=media_type)
    if category.isdigit():
        items = items.filter(category_id=category)
    return render(request, "media_library/library.html", {
        "items": items, "categories": Category.objects.all(),
        "query": query, "selected_type": media_type, "selected_category": category,
    })

def media_detail(request, pk):
    item = get_object_or_404(MediaItem.objects.select_related("category"), pk=pk)
    MediaItem.objects.filter(pk=pk).update(views=F("views") + 1)
    return render(request, "media_library/detail.html", {"item": item})

def upload_media(request):
    if request.method == "POST":
        form = MediaItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, "Your media has been added to the library.")
            return redirect(item.get_absolute_url())
    else:
        form = MediaItemForm()
    return render(request, "media_library/upload.html", {"form": form})
