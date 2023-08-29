from django.db import models
from django.utils import timezone

class Member(models.Model):
    membership_choice = [
        ('normal', 'Normal'),
        ('special', 'Special')
    ]
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    membership_type = models.CharField(
        max_length=10, choices=membership_choice)
    validity_date = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now)
