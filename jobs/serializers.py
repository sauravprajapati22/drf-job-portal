from rest_framework import serializers
from .models import job

class Jobserializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = "__all__"
        read_only_fields = ['created_by']

    