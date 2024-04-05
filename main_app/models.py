from django.db import models
from django.urls import reverse

# Create your models here.


class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        # redirect to detail url path
        return reverse('finch-detail', kwargs={'finch_id': self.id})
        # int:finch_id & POST newly created finch
        # return reverse('', kwargs={'pk': self.pk})
