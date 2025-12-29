from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, submit_contact

router = DefaultRouter()
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', submit_contact),
]
