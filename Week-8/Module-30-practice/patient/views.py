from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers

# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
