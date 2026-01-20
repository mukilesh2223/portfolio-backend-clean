from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from .models import Project, Contact
from .serializers import ProjectSerializer, ContactSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("-id")
    serializer_class = ProjectSerializer


@api_view(["POST"])
def submit_contact(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        contact = serializer.save()

        name = contact.name
        email = contact.email
        message = contact.message

        # --------------------------
        # 1️⃣ ADMIN NOTIFICATION
        # --------------------------
        send_mail(
            subject=f"New Message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # --------------------------
        # 2️⃣ AUTO REPLY TO USER (FIXED)
        # --------------------------
        auto_reply_message = f"""
Hi {name},

Thank you for contacting me!

I have received your message and will get back to you shortly.

Your Message:
--------------------------------
{message}
--------------------------------

Regards,
Mugilesh
Full Stack Python Developer
"""

        email_message = EmailMessage(
            subject="Thank you for contacting me!",
            body=auto_reply_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
            reply_to=[settings.DEFAULT_FROM_EMAIL],  # IMPORTANT
        )

        email_message.send(fail_silently=False)

        return Response({"success": True, "message": "Email sent successfully"})

    return Response(serializer.errors, status=400)
