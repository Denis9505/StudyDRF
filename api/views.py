from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Transaction, UserProfile, Category
from .serializers import TransactionSerializer, ProfileSerializer, CategoriesSerializer
# Create your views here.

class ProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all().order_by('time')
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )
    filter_fields = ['count', 'date', 'organization']
    ordering_fields = ['count', 'date', 'organization']
        

class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by('kind')
    serializer_class = CategoriesSerializer
    permission_classes = (IsAuthenticated, )
    filter_fields = ['title']
    ordering_fields = ['title']
