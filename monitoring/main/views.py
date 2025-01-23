from django.shortcuts import render
from django.http import JsonResponse
from .models import Incedent

def incedents_(request):
    incedents = Incedent.objects.all().order_by('-uptime')
    data = [
        {
            'machine_status': incedent.machine_status,
            'incedent_type': incedent.incedent_type,
            'time': incedent.uptime,
        }
        for incedent in incedents
    ]
    return JsonResponse({'incedents': data})

def incedent_template(request):
    return render(request, 'main/index.html')