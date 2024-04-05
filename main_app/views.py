from django.shortcuts import render
from .models import Finch

# Create your views here.
finches = [
    {'species': 'Zebra Finch', 'color': 'Gray', 'size': 'Small'},
    {'species': 'Gouldian Finch', 'color': 'Multicolored', 'size': 'Small'},
    {'species': 'Society Finch', 'color': 'Brown', 'size': 'Small'},
    {'species': 'Spice Finch', 'color': 'Brown', 'size': 'Small'},
    {'species': 'Star Finch', 'color': 'Red', 'size': 'Small'}
]

# Define a function to simulate a view that returns finch data


def get_finch_data():
    # In a real application, you would retrieve data from a database
    # Here, we are just returning the simulated data
    return finches


# Simulate calling the view function and print the result
print(get_finch_data())


def home(request):

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    # tell the model to find all the rows in the finches table!
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })

