from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from .models import Project, Contact
from .serializers import ProjectSerializer, ContactSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer


@api_view(['POST'])
def submit_contact(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        contact = serializer.save()

        # Extract data from saved contact
        name = contact.name
        email = contact.email
        message = contact.message

        # --------------------------
        # 1️⃣ ADMIN NOTIFICATION
        # --------------------------
        send_mail(
            subject=f"New Message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email="infomugi123@gmail.com",
            recipient_list=["infomugi123@gmail.com"],
            fail_silently=False,
        )

        # --------------------------
        # 2️⃣ AUTO REPLY TO USER
        # --------------------------
        auto_reply_message = f"""
Hi {name}, 👋

Thank you for contacting me!

I have received your message and will get back to you shortly.
If it's urgent, feel free to reach out again.

Your Message:
------------------------------------------------
{message}
------------------------------------------------

Regards,
Mugilesh
Fullstack Python Developer
"""

        send_mail(
            subject="Thank you for contacting me!",
            message=auto_reply_message,
            from_email="infomugi123@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({"message": "Success"})

    return Response(serializer.errors, status=400)
