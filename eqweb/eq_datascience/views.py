from django.shortcuts import render
from .models import Cuenta, SalesAccountTrimester
from django.views import generic

# Create your views here.


def index(request):

    list_cuenta = Cuenta.objects.all()

    return render(
        request,
        'base_generic.html',
        context={'FromIndexAccount': list_cuenta}
    )

#
# def show_data(request):
#
#     list_cuenta = Cuenta.objects.all()
#
#     return render(
#         request,
#         'base_generic.html',
#         context={'MuestraCuenta': list_cuenta}
#     )


class CuentaDetailView(generic.DetailView):
    model = Cuenta
    list_cuenta = {'MuestraCuenta': Cuenta.objects.all()}


class AccountTrimesterDetailView(generic.DeleteView):
    model = SalesAccountTrimester
    list_sales = {'MuestraCuenta': SalesAccountTrimester.objects.all()}

