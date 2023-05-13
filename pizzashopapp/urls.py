from django.urls import path
from . import views, apis
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),

    # Авторизация пользователя
    path('pizzashop/sing-in/', LoginView.as_view(
            template_name='pizzashopapp/sing_in.html'), name='pizzashop-sing-in'),

    # Выход с системы
    path('pizzashop/sing-out/', LogoutView.as_view(
            next_page='/',
            template_name='pizzashopapp/sing_out.html'), name='pizzashop-sing-out'),

    # Переход после авторизации
    path('pizzashop/', views.pizzashop_home, name='pizzashop_home'),

    # Регистрация пользователя
    path('pizzashop/sing-up/', views.pizzashop_sing_up, name='pizzashop_sing_up'),
    
    # Переход к аккаунту
    path('pizzashop/account/', views.pizzashop_account, name='pizzashop_account'),

    # Переход к пиццам
    path('pizzashop/pizza/', views.pizzashop_pizza, name='pizzashop_pizza'),

    # Добавление пиццы
    path('pizzashop/pizza/add/', views.pizzashop_add_pizza, name='pizzashop_add_pizza'),

    # Редактирование пиццы
    path('pizzashop/pizza/edit/<int:pizza_id>/', views.pizzashop_edit_pizza, name='pizzashop_edit_pizza'),
    
    # API
    path('api/client/pizzashops/', apis.client_get_pizzashop),
    path('api/client/pizzas/<int:pizzashop_id>/', apis.client_get_pizzas),


]
