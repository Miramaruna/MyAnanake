from rest_framework import serializers

from .models import Home, Personal

class HomeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

class PersonalSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'
    
# class SettingsUpdateSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Settings
#         fields = ['id', 'description', 'created']