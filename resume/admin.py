from django.contrib import admin

# Register your models here.
from .models import GalleryImage  # Import your model


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
