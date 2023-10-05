from rest_framework import serializers

from product.models import Product, Review, Category


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)
    price = serializers.IntegerField()
    category = serializers.IntegerField()

    class Meta:
        model = Product
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=300)
    product = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = "__all__"
