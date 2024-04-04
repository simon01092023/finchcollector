from django.shortcuts import render

# Create your views here.
finches = [
    {'id': 1, 'species': 'Zebra Finch', 'color': 'Gray', 'size': 'Small'},
    {'id': 2, 'species': 'Gouldian Finch', 'color': 'Multicolored', 'size': 'Small'},
    {'id': 3, 'species': 'Society Finch', 'color': 'Brown', 'size': 'Small'},
    {'id': 4, 'species': 'Spice Finch', 'color': 'Brown', 'size': 'Small'},
    {'id': 5, 'species': 'Star Finch', 'color': 'Red', 'size': 'Small'}
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
    # finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })
