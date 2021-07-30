from django.db import models


class PetOwner(models.Model):
    """Pet Owner."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField(max_length=1000)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    """Pet model."""

    name = models.CharField(max_length=255)

    PET_TYPES = (
        ("cat", "Cat"),
        ("dog", "Dog"),
        ("rabbit", "Rabbit"),
        ("parrot", "Parrot"),
    )
    type = models.CharField(max_length=50, choices=PET_TYPES, default="dog")
    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    owner = models.ForeignKey(PetOwner, on_delete=models.PROTECT, related_name="pets")

    def __str__(self):
        return f"{self.name}, {self.type}"
