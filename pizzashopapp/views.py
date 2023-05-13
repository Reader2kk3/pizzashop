from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, PizzaShopForm, UserFormEdit, PizzaForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Pizza

# Главная страница
def home(request):
    return redirect(pizzashop_home)

# Главная страница
@login_required(login_url='/pizzashop/sing-in/')
def pizzashop_home(request):
    return redirect(pizzashop_pizza)

# Регистрация пользователя
def pizzashop_sing_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES)

        if user_form.is_valid() and pizzashop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizzashop = pizzashop_form.save(commit=False)
            new_pizzashop.owner = new_user
            new_pizzashop.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password'],
            ))

            return redirect(pizzashop_home)

    context = {'user_form': user_form, 'pizzashop_form': pizzashop_form}
    return render(request, 'pizzashopapp/sing_up.html', context)


# Редактирование аккаунта
@login_required(login_url='/pizzashop/sing-in/')
def pizzashop_account(request):
    user_form = UserFormEdit(instance=request.user)
    pizzashop_form = PizzaShopForm(instance=request.user.pizzashop) # related_name (pizzashop)

    if request.method == 'POST':
        user_form = UserFormEdit(request.POST, instance=request.user)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES, instance=request.user.pizzashop)

        if user_form.is_valid() and pizzashop_form.is_valid():
            user_form.save()
            pizzashop_form.save()

    context = {'user_form': user_form, 'pizzashop_form': pizzashop_form}
    return render(request, 'pizzashopapp/account.html', context)


# Редактирование пицц
@login_required(login_url='/pizzashop/sing-in/')
def pizzashop_pizza(request):
    pizzas = Pizza.objects.filter(owner=request.user.pizzashop).order_by("-id")



    context = {'pizzas': pizzas}
    return render(request, 'pizzashopapp/pizza.html', context)

# Добавление пиццы
@login_required(login_url='/pizzashop/sing-in/')
def pizzashop_add_pizza(request):
    form = PizzaForm()

    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES)

        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.owner = request.user.pizzashop
            pizza.save()
            return redirect(pizzashop_pizza)

    context = {'form': form}
    return render(request, 'pizzashopapp/add_pizza.html', context)

# Редактирование пиццы
def pizzashop_edit_pizza(request, pizza_id):
    form = PizzaForm(instance=Pizza.objects.get(id=pizza_id))

    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES, instance=Pizza.objects.get(id=pizza_id))

        if form.is_valid():
            pizza = form.save()
            return redirect(pizzashop_pizza)

    context = {'form': form}
    return render(request, 'pizzashopapp/edit_pizza.html', context)
