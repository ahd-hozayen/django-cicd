from django.db import models

class Emp(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
