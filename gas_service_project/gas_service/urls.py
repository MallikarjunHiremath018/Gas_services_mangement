from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ServiceRequestViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
