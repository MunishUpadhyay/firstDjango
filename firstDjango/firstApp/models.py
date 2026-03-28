from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_CHOICE_TYPE = [
        ('ML', 'Masala Chai'),
        ('GR', 'Ginger Chai'),
        ('KL', 'Kashmiri Chai'),
        ('PL', 'Plain Chai'),
        ('EL', 'Elaichi Chai'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_CHOICE_TYPE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
