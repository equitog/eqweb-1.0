from django.shortcuts import render
from .models import Cuenta, SalesAccountTrimester
from django.views import generic
from django.http import JsonResponse
# Create your views here.


def index(request):

    list_cuenta = Cuenta.objects.all()

    return render(
        request,
        'base_generic.html',
        context={'FromIndexAccount': list_cuenta}
    )


def get_data(request, *args, **kwargs):
    data = {"year": [2018, 2019],
            "sales": [340, 232],
            "buy": [394, 345]}
    return JsonResponse(data)


class CuentaDetailView(generic.DetailView):
    model = Cuenta
    list_cuenta = {'MuestraCuenta': Cuenta.objects.all()}


class SalesAccountTrimesterListView(generic.ListView):
    model = SalesAccountTrimester
