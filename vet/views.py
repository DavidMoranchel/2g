from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Serializers
from .serializers import PetOwnersListSerializer, PetOwnerSerializer, PetsListSerializer

# Models
from .models import PetOwner, Pet


class PetOwnersListCreate(APIView):
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


class PetOwnerDetailAPIView(APIView):

    serializer_class = PetOwnerSerializer

    def get(self, request, pk):

        owner = get_object_or_404(PetOwner, id=pk)
        serializer = self.serializer_class(owner)
        return Response(serializer.data)


class PetsList(APIView):
    """
    View to list all pets in the system.
    """

    serializer_class = PetsListSerializer

    def get(self, request):

        pets_queryset = Pet.objects.all()
        serializer = self.serializer_class(pets_queryset, many=True)

        return Response(data=serializer.data)
