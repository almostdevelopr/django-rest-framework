from rest_framework import serializers
from home.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        """An inner class ro know which model to serialize."""
        model = Person
        # exclude = ['name']
        fields = "__all__"
