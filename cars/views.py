from django.shortcuts import render
from cars.models import Car

# Create your views here.
def cars_view(request):
    #cars = Car.objects.all() # Retorna todos os registros do
    
    # cars = Car.objects.filter(brand__name='Fiat') # Retorna os registros onde a band é Fiat utilizando duplo underscore para pegar o nome na tabela que se vincula a Car
    
    cars = Car.objects.filter(model__contains='Fiat') # Retorna os registros que contém Fiat no nome do modelo (like 'nome%' no SQL)
    return render(
        request,
        'cars.html',
        {'cars':cars}
    )