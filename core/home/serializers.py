from rest_framework import serializers
from home.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        """An inner class ro know which model to serialize."""
        model = Person
        # exclude = ['name']
        fields = "__all__"

    def validate(self, data):
        speacial_characters = "!@#$%^&*()_+?_+,<>/"
        if any(c in speacial_characters for c in data['name']):
            raise serializers.ValidationError(
                "name cannot contain special characters")

        if data['age'] < 18:
            raise serializers.ValidationError("age should be greater than 18")

        return data
