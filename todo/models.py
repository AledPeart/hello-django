from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # sets our own function to overriode how thw default django
    # model sets the string names
    def __str__(self):
        return self.name
