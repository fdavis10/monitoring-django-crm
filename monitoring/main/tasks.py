import requests
from celery import shared_task
from .models import Machine, Incedent
from django.utils import timezone
from datetime import timedelta

@shared_task
def get_status():
    try:
        resp = requests.get('http://localhost:5000/datas')
        if resp.status_code == 200:
            data = resp.json()
            status = Machine.objects.create(
                    cpu=data['cpu'],
                    memory = int(data['memory'].strip('%')),
                    disk = int(data['disk'].strip('&')),
                    uptime = data['uptime']
                )
        
        check_inc(status)

    except Exception as error:
        print(f'Error: {error}')
    
def check_inc(status):
    now = timezone.now()

    # CPU 
    if status.cpu > 85:
        cpu_inc = Incedent.objects.filter(machine_status__cpu__gt=85,
                                          uptime__gte=now - timedelta(minutes=30)
                                          )
        if not cpu_inc.exists():
            Incedent.objects.create(machine_status = status, incident_type = 'CPU')

    # MEM
    if status.memory > 90:
        mem_inc = Incedent.objects.filter(machine_status__memory__gt=90,
                                          uptime__gte=now - timedelta(minutes=30))
        if not mem_inc.exists():
            Incedent.objects.create(machine_status=status, incedent_type = 'MEMORY')
    
    # DISK
    if status.disk > 95:
        disk_inc = Incedent.objects.filter(machine_status__disk__gt=95,
                                          uptime__gte=now - timedelta(hours=2))
        if not disk_inc.exists():
            Incedent.objects.create(machine_status=status, incedent_type = 'DISK')
            

@shared_task
def add(x, y):
    return x + y
    