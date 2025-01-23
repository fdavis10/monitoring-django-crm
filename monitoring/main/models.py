from django.db import models

class Machine(models.Model):
    machine_name = models.CharField(max_length=100)
    cpu = models.IntegerField()
    memory = models.CharField(max_length=10)
    disk = models.CharField(max_length=10)
    uptime = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.uptime}'

class Incedent(models.Model):
    machine_status = models.ForeignKey(Machine, on_delete=models.CASCADE)
    incedent_type = models.CharField(max_length=20)
    uptime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.incedent_type} - {self.uptime}'
