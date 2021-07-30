from rest_framework.views import APIView
from rest_framework.response import Response


# Serializers
from .serializers import PetOwnersListSerializer, PetsListSerializer

# Models
from .models import PetOwner, Pet


class PetOwnersList(APIView):
    """
    View to list all pet owners in the system.
    """

    serializer_class = PetOwnersListSerializer

    def get(self, request):

        # owners = [
        #     {"id": owner.id, "first_name": owner.first_name}
        #     for owner in PetOwner.objects.all()
        # ]

        owners_queryset = PetOwner.objects.all()
        serializer = self.serializer_class(owners_queryset, many=True)

        return Response(data=serializer.data)


class PetsList(APIView):
    """
    View to list all pets in the system.
    """

    serializer_class = PetsListSerializer

    def get(self, request):

        pets_queryset = Pet.objects.all()
        serializer = self.serializer_class(pets_queryset, many=True)
        # pets = [
        #     {
        #         "id": pet.id,
        #         "name": pet.name,
        #         "type": pet.type,
        #         "owner": f"{pet.owner.first_name} {pet.owner.last_name}",
        #     }
        #     for pet in pets_queryset
        # ]

        return Response(data=serializer.data)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Serializers
# from .serializers import PetOwnerListSerializer

# serializer_class = PetOwnerListSerializer

# def get(self, request, format=None):
#     """
#     Return a list of all pet owners.
#     """
#     owners = PetOwner.objects.all()
#     serializer = self.serializer_class(owners, many=True)

#     return Response(serializer.data)
