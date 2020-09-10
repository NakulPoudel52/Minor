from django.db import models

# Create your models here.
class notification(models.Model):
    to_user = models.CharField(max_length=64)
    for_user = models.CharField(max_length=64)
    is_view = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.to_user} send to {self.for_user}"
class disease(models.Model):
    Disease = models.CharField(max_length=64)
    Precaution_1 = models.CharField(max_length=64,blank=True)
    Precaution_2 = models.CharField(max_length=64,blank=True)
    Precaution_3 = models.CharField(max_length=64,blank=True)
    Precaution_4 = models.CharField(max_length=64,blank=True)

    def __str__(self):
        return f"{self.Disease} has precautions as:{self.Precaution_1}..."
    