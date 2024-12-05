from django.shortcuts import render
from .models import Taxi


def taxi_page_view(request):
    if request.method == "POST":
        taxi_name = request.POST.get('taxi_name')
        license = request.POST.get('license')
        driver = request.POST.get('driver')
        capacity = request.POST.get('capacity')
        model = request.POST.get('model')
        status = request.POST.get('status')
        Taxi.objects.create(taxi_name=taxi_name, license=license, driver=driver, capacity=capacity, model=model,
                            status=status)

    else:
        taxi_name = request.GET.get('taxi_name')
        license = request.GET.get('license')
        driver = request.GET.get('driver')
        capacity = request.GET.get('capacity')
        model = request.GET.get('model')
        status = request.GET.get('status')
    return render(request, 'taxi/taxi.html')

    taxi = Taxi.objects.all()
    context = {'taxi': taxi}
    return render(request, 'taxi/taxi.html', context)
