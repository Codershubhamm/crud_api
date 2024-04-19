from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['id',"name"]
        # exclude = ('name')
        fields = "__all__"