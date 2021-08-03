from rest_framework import serializers
from .models import PetOwner


class PetOwnersListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)


class PetOwnerSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    address = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    def create(self, validated_data):
        return PetOwner.objects.create(**validated_data)


class PetOwnerUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.save()
        return instance


class PetsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=50)
