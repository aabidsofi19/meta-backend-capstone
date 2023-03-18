from rest_framework import serializers
from . import models


class MenuSerializer(serializers.ModelSerializer) :

    class Meta :
        model = models.Menu
        fields = ["id" , "title","price","inventory"]

    