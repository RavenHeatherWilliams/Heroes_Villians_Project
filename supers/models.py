from unittest.util import _MAX_LENGTH
from django.db import models
# from super_types.models import Super_Types


# Create your models here.
class Supers(models.Model):
    name = models.Charfield(max_length=255)
    alter_ego = models.Charfield(max_length=255)
    primary_ability = models.Charfield(max_length=255)
    secondary_ability = models.Charfield(max_length=255)
    catchphrase = models.Charfield(max_length=255)
    # super_type = models.ForeignKey(Super_Types, on_delete=models.cascade)