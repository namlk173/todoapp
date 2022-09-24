from rest_framework import serializers
from base.api.serializer import MyUserserializer
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    user = MyUserserializer(read_only=True)

    class Meta:
        model = ToDo
        fields = "__all__"

    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.__dict__.update(**validated_data)
        instance.save()

        return instance