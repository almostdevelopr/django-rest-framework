from dataclasses import fields
from rest_framework import serializers
from home.models import Color, Person


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name']


class PersonSerializer(serializers.ModelSerializer):

    color = ColorSerializer()

    class Meta:
        """An inner class ro know which model to serialize."""
        model = Person
        fields = "__all__"
        # depth = 1

    def validate(self, data):
        speacial_characters = "!@#$%^&*()_+?_+,<>/"
        if any(c in speacial_characters for c in data['name']):
            raise serializers.ValidationError(
                "name cannot contain special characters")

        if data['age'] < 18:
            raise serializers.ValidationError("age should be greater than 18")

        return data
