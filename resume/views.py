
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse


from .models import GalleryImage


def index(request):
    """
    Home page which is the first page that viewers see when they open the site.

    """
    return render(request, 'resume/index.html')


def sponsors(request):
    """
    Sponsors page displaying contact information and current sponsors.
    Handles contact form submissions and sends emails via Gmail SMTP.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Email content
        subject = f"(PARTNER) New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = "anele@an-racing.com"  # Should match EMAIL_HOST_USER
        # Recipient email, could be the same
        recipient_list = ["anele@an-racing.com"]

        try:

            send_mail(subject, body, from_email, recipient_list)
            messages.success(
                request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(
                request, "There was an error sending your message. Please try again.")

        return redirect("sponsors")  # Prevent resubmission on refresh

    return render(request, "resume/sponsors.html")


def contact(request):
    """
    Contact page
    """
    return render(request, 'resume/contact.html')


def stats(request):
    """ Statisitcs page """
    return render(request, 'resume/stats.html')


def services(request):
    """Page to offer website making services for others"""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            # Email content
            subject = f"(QUOTE) New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            # Use your email (from settings)
            from_email = "anele@an-racing.com"
            # The recipient email(s)
            recipient_list = ["anele@an-racing.com"]

            try:
                # Send the email
                send_mail(subject, body, from_email, recipient_list)
                messages.success(
                    request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(
                    request, "There was an error sending your message. Please try again.")
        else:
            messages.error(request, "Please fill out all fields correctly.")

        return redirect("services")  # Prevent resubmission on refresh

    return render(request, "resume/services.html")


def portfolio(request):
    """
    Portfolio page displaying results and other career-important information,
    including a gallery of uploaded images.
    """
    images = GalleryImage.objects.all()  # Fetch all uploaded images
    return render(request, 'resume/portfolio.html', {'images': images})


def gallery(request):
    """
    Displays the gallery page with album names.
    """
    albums = GalleryImage.objects.values_list('album', flat=True).distinct()
    return render(request, 'resume/gallery.html', {'albums': albums})


def fetch_album_images(request):
    """
    AJAX endpoint to fetch images for a selected album.
    """
    album_name = request.GET.get('album')
    images = GalleryImage.objects.filter(album=album_name)
    data = [{'url': img.image.url, 'title': img.title} for img in images]
    return JsonResponse({'images': data})
