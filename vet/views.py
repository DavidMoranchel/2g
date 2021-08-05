from rest_framework import generics

# Serializers
from .serializers import (
    # Pet Owner serializers
    PetOwnerModelSerializer,
    PetOwnersListModelSerializer,
    # Pet serializers
    PetModelSerializer,
    PetListModelSerializer,
    # Pet dates serializers
    PetDateModelSerializer,
    PetDateListModelSerializer,
    PetDatePetRetrieveModelSerializer,
    PetDatePartialUpdateModelSerializer,
)

# Models
from .models import PetOwner, Pet, PetDate


class PetOwnersListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListModelSerializer

    def get_queryset(self):

        first_name_filter = self.request.GET.get("first_name")
        filters = {}
        if first_name_filter:
            filters["first_name__icontains"] = first_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer

        return serializer_class


class PetOwnersDatesListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset(self):
        owner_id = self.kwargs["pk"]
        filters = {}
        if owner_id:
            filters["pet__owner_id"] = owner_id

        return self.queryset.filter(**filters)


class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer


class PetListCreateAPIView(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetModelSerializer

        return serializer_class


class PetDateListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset(self):
        pet_id = self.request.GET.get("pet")
        owner_id = self.request.GET.get("owner")
        filters = {}
        if pet_id:
            filters["pet_id"] = pet_id

        if owner_id:
            filters["pet__owner_id"] = owner_id

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetDateModelSerializer

        return serializer_class


class PetDateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    http_method_names = ["get", "patch", "delete"]
    queryset = PetDate.objects.all()
    serializer_class = PetDatePetRetrieveModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "PATCH":
            serializer_class = PetDatePartialUpdateModelSerializer

        return serializer_class


# ENDPOINTS
# 1. Create date -- DONE
# 2. List all dates -- DONE
# 3. Partial Update date (datetime, type) -- DONE
# 4. Remove date -- DONE
# 5. Retrieve with Pet Information -- DONE
# 6. List dates by pet
# 7. List dates by owner
