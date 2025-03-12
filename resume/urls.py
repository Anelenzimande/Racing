from django.urls import path
from . import views
from .views import gallery, fetch_album_images


urlpatterns = [
    path('', views.index, name='index'),  # Maps the root URL to the index view
    path('resume/portfolio/', views.portfolio, name='portfolio'),
    path('resume/sponsors/', views.sponsors, name='sponsors'),
    path('resume/contact/', views.contact, name='contact'),
    path('resume/stats/', views.stats, name='stats'),
    path('resume/services/', views.services, name='services'),
    path('resume/gallery/', views.gallery, name='gallery'),
    path('gallery/', gallery, name='gallery'),
    path('gallery/fetch-images/', fetch_album_images, name='fetch_album_images'),

]
