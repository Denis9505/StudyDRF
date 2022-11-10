from rest_framework import serializers

from .models import Transaction, UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Transaction
        fields = '__all__'
