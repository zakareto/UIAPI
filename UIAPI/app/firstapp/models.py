from django.db import models

# Create your models here.

class Dogs(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=250, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dogs'


class Types(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'

class DogFoods(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    brand = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dog_foods'


class Videogames(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    rating_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videogames'


class Rating(models.Model):
    esrb = models.CharField(max_length=50, blank=True, null=True)
    pegi = models.CharField(max_length=50, blank=True, null=True)
    cero = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'

