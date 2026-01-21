from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['user_name', 'email', 'created_at']
    
    def validate_user_name(self, value):
        for i in value:
            if i.isdigit():
                raise serializers.ValidationError("Username should not contain numbers.")