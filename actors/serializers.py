from dataclasses import fields
from pyexpat import model
from re import A
from rest_framework import serializers
from.models import Actor

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
         model=Actor
         fields='__all__'
