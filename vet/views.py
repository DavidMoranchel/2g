from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Serializers
from .serializers import (
    PetOwnerSerializer,
    PetOwnerUpdateSerializer,
    PetOwnersListSerializer,
    PetsListSerializer,
)

# Models
from .models import PetOwner, Pet


class PetOwnersListCreateAPIView(APIView):
    """
    View to list all pet owners in the system.
    """

    serializer_class = PetOwnersListSerializer

    def get(self, request):

        owners_queryset = PetOwner.objects.all()
        serializer = self.serializer_class(owners_queryset, many=True)

        return Response(data=serializer.data)

    def post(self, request):

        serializer = PetOwnerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_instance = serializer.save()

        print(created_instance.__dict__)

        return Response({})


class PetOwnerRetrieveUpdateDestroyAPIView(APIView):
    """
    View to retrieve a pets by id.
    """

    serializer_class = PetOwnerSerializer

    def get(self, request, pk):

        owner = get_object_or_404(PetOwner, id=pk)
        serializer = self.serializer_class(owner)
        return Response(serializer.data)

    def patch(self, request, pk):

        owner = get_object_or_404(PetOwner, id=pk)
        serializer = PetOwnerUpdateSerializer(instance=owner, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        serialized_instance = self.serializer_class(updated_instance)
        return Response(serialized_instance.data)

    def delete(self, request, pk):

        owner = get_object_or_404(PetOwner, id=pk)
        owner.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PetsListAPIView(APIView):
    """
    View to list all pets in the system.
    """

    serializer_class = PetsListSerializer

    def get(self, request):

        pets_queryset = Pet.objects.all()
        serializer = self.serializer_class(pets_queryset, many=True)

        return Response(data=serializer.data)
