from django.db import models
from django.urls import reverse
from datetime import date


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    toys = models.ManyToManyField(Toy)
    is_hungry = models.BooleanField(default=True)

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

        # Add the current date
        # Set the last_updated_date field to today's date
        self.last_updated_date = date.today()
        self.save()


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

    class Meta:
        ordering = ['-date']
