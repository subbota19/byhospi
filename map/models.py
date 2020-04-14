from django.db import models


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    population = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
