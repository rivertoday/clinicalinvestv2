__author__ = 'jeremyjiang'
from rest_framework import serializers

from myusers.models import MyUser
from .models import ClinicalProjects

class ClinicalProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalProjects
        fields = "__all__"
