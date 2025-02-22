from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from .models import Customer, ServiceRequest
from .serializers import CustomerSerializer, ServiceRequestSerializer
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ServiceRequestListView(APIView):
    permission_classes = [IsAuthenticated]  # Now authentication is required

    def get(self, request):
        requests = ServiceRequest.objects.all()
        serializer = ServiceRequestSerializer(requests, many=True)
        return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAuthenticated])
    def update_status(self, request, pk=None):
        service_request = get_object_or_404(ServiceRequest, pk=pk)
        service_request.status = request.data.get('status', service_request.status)
        if service_request.status == 'Resolved':
            service_request.resolved_at = now()
        service_request.save()
        return Response({'status': 'Service request updated'})


def home(request):
    return HttpResponse("Welcome to the Gas Service API")

