from django.shortcuts import render

# Create your views here.


def index(request):
    return render(
        request,
        'index.html',
        context={'num_test': 10}
    )


def show_data(request):
    return render(
        request,
        'show_data.html',
        context={'num_test': 10}
    )