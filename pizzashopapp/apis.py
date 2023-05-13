from django.http import JsonResponse

from .models import PizzaShop, Pizza
from .serializers import PizzaShopSerializer, PizzaSerializer

def client_get_pizzashop(request):
    pizzashops = PizzaShopSerializer(
        PizzaShop.objects.all().order_by('-id'),
        many=True,
        context={'request': request}
    ).data

    context = {}
    return JsonResponse({'pizzashops': pizzashops})

def client_get_pizzas(request, pizzashop_id):
    pizzas = PizzaSerializer(
        Pizza.objects.all().filter(owner_id=pizzashop_id).order_by('-id'),
        many=True,
        context={'request': request}
    ).data

    return JsonResponse({'pizzas': pizzas})
    