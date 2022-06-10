from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Livre

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = '__all__'