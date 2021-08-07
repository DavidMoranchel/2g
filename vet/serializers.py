from django.db import models
from rest_framework import serializers
from .models import PetOwner, Pet, PetDate


class PetOwnersListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name", "email"]


class PetListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name", "owner"]
        depth = 1


class PetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name", "type", "owner"]


class PetDateListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "pet"]


class PetDateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "pet"]


class PetDatePetRetrieveModelSerializer(serializers.ModelSerializer):

    pet = PetModelSerializer()

    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "pet"]


class PetDatePartialUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ["datetime", "type"]


class PetOwnerModelSerializer(serializers.ModelSerializer):

    pets = PetModelSerializer(many=True)

    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name", "address", "phone", "email", "pets"]


from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validate_data):
        # validate_data["is_staff"] = True
        user = User.objects.create_user(**validate_data)

        return user
