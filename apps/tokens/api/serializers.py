from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer
)
from apps.tokens.models import *


class TokenSerializer(ModelSerializer):    
    # seller_user_id = serializers.CharField(required=False)
    class Meta:
        model = Token
        read_only_fields = ['token']
        fields = '__all__'
    