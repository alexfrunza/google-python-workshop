from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    location = models.ForeignKey("aplicatie1.Location", on_delete=models.CASCADE)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name}"
