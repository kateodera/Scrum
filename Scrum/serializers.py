from rest_framework import serializers
from .models import User, Task, Sprint

# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

# Serializers define the API representation.


class SprintSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Sprint
        fields ="__all__"

# Serializers define the API representation.


class SprintTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        fields = [
            'id',
            'title'
        ]


# Serializers define the API representation.

class TaskSerializer(serializers.ModelSerializer):
    sprint = SprintTaskSerializer()

    class Meta:
        model = Task
        fields = "__all__"

