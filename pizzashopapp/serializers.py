from rest_framework import serializers
from .models import PizzaShop, Pizza

class PizzaShopSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    # Полный путь для изображений
    def get_logo(self, pizzashop):
        request = self.context.get('request')
        logo_url = pizzashop.logo.url
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = PizzaShop
        fields = ('id', 'name', 'phone', 'address', 'logo')

class PizzaSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    # Полный путь для изображений
    def get_img(self, pizza):
        request = self.context.get('request')
        img_url = pizza.img.url
        return request.build_absolute_uri(img_url)

    class Meta:
        model = Pizza
        fields = ('id', 'name', 'short_description', 'img', 'price')