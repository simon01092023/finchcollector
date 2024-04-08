from django.db import models
from django.urls import reverse


class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        # Redirect to detail URL path
        return reverse('finch-detail', kwargs={'finch_id': self.id})

    def update_hunger_status(self):
        # Check if any feedings exist for this finch
        if self.feeding_set.exists():
            self.is_hungry = False
        else:
            self.is_hungry = True

        # Save the updated status
        self.save()

    # Initialize is_hungry attribute
    is_hungry = models.BooleanField(default=True)


MEALS = (("B", "Breakfast"), ("L", "Lunch"), ("D", "Dinner"))


class Feeding(models.Model):
    date = models.DateField("feeding date")
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0],
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
