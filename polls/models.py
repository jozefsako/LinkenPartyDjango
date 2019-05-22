# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import math  

class Events(models.Model):
    id_event = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(
        'AUsers', models.DO_NOTHING, db_column='id_user')
    name_event = models.CharField(max_length=250)
    theme_event = models.CharField(max_length=250)
    creation_date = models.DateTimeField()
    location_map = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    address_event = models.TextField(blank=True, null=True)
    size_hosting = models.IntegerField(blank=True, null=True)
    state_event = models.CharField(max_length=50, blank=True, null=True)
    description_event = models.TextField(blank=True, null=True)
    type_event = models.CharField(max_length=50)
    version_number = models.IntegerField()
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'events'


class EventsWithoutID(models.Model):
    id_user = models.ForeignKey(
        'AUsers', models.DO_NOTHING, db_column='id_user')
    name_event = models.CharField(max_length=250)
    theme_event = models.CharField(max_length=250)
    creation_date = models.DateTimeField()
    location_map = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    address_event = models.TextField(blank=True, null=True)
    size_hosting = models.IntegerField(blank=True, null=True)
    state_event = models.CharField(max_length=50, blank=True, null=True)
    description_event = models.TextField(blank=True, null=True)
    type_event = models.CharField(max_length=50)
    version_number = models.IntegerField()
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'events'


class Participations(models.Model):
    id_participation = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(
        'AUsers', models.DO_NOTHING, db_column='id_user')
    id_event = models.ForeignKey(
        'Events', models.DO_NOTHING, db_column='id_event')
    participation_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'participations'


class ParticipationsWithouID(models.Model):
    id_user = models.ForeignKey(
        'AUsers', models.DO_NOTHING, db_column='id_user')
    id_event = models.ForeignKey(
        'Events', models.DO_NOTHING, db_column='id_event')
    participation_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'participations'


class AUsers(models.Model):
    id_user = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    username = models.CharField(max_length=50)
    type_user = models.CharField(max_length=1)
    registration_date = models.DateField()
    birthdate = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1)
    version_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ausers'


class AUsersWithouID(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    username = models.CharField(max_length=50)
    type_user = models.CharField(max_length=1)
    registration_date = models.DateField()
    birthdate = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1)
    version_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ausers'


# class Geolocalisation:
    
#     RAD_MILES = 3959
#     RAD_KM = 6371

#     @staticmethod
#     def calculateRadius(x1, y1, x2, y2):
#         radius = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
#         return radius

#     @staticmethod
#     def convertDistanceIntoRadKM(distance):
#         r = distance / RAD_KM
#         return r

#     @staticmethod
#     def convertDistanceIntoRadMILES(distance):
#         r = distance / RAD_MILES
#         return r