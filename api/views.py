from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Transaction, UserProfile
from .serializers import TransactionSerializer, ProfileSerializer
# Create your views here.

class ProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all().order_by('time')
    serializer_class = TransactionSerializer
        