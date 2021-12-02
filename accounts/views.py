from django.shortcuts import render


# Create your views here.

def panel(request):
    return render(request, 'panel.html')


def show404(request):
    return render(request, '404page.html')
