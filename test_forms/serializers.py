# REST FRAMEWORK imports
from rest_framework import serializers

# LOCAL APP imports
from . import models

class TestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        exclude = (
            None,
        )
        model = models.Test
        
