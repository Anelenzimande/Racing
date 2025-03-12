from django.db import models

# Create your models here.

from django.db import models
from cloudinary.models import CloudinaryField


class GalleryImage(models.Model):

    # Manually entered album name
    album = models.CharField(max_length=255, default="2024")

    # Title of the gallery image, optional field, can be left blank
    title = models.CharField(max_length=255, blank=True)

    # Cloudinary field to store the image, handles image upload to Cloudinary
    image = CloudinaryField('image')

    # Automatically records the date and time when the image was uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # String representation of the model

    def __str__(self):
        return f"{self.album} - {self.title}" if self.title else f"{self.album} - Gallery Image"
