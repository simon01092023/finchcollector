from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm

# # Create your views here.
# finches = [
#     {'species': 'Zebra Finch', 'color': 'Gray', 'size': 'Small'},
#     {'species': 'Gouldian Finch', 'color': 'Multicolored', 'size': 'Small'},
#     {'species': 'Society Finch', 'color': 'Brown', 'size': 'Small'},
#     {'species': 'Spice Finch', 'color': 'Brown', 'size': 'Small'},
#     {'species': 'Star Finch', 'color': 'Red', 'size': 'Small'}
# ]

# # Define a function to simulate a view that returns finch data


# def get_finch_data():
#     # In a real application, you would retrieve data from a database
#     # Here, we are just returning the simulated data
#     return finches


# # Simulate calling the view function and print the result
# print(get_finch_data())


def home(request):

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def disassoc_toy(request, finch_id, toy_id):
    finch = Finch.objects.get(id=finch_id)
    finch.toys.remove(toy_id)
    return redirect('finch-detail', finch_id=finch_id)

# finches/<int:finch_id>/assoc_toy/<int:toy_id>/


def assoc_toy(request, finch_id, toy_id):
    print(finch_id, toy_id)
    finch = Finch.objects.get(id=finch_id)
    finch.toys.add(toy_id)  # adding a row to 2 foriegn keys table in sql
    return redirect('finch-detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch
    # disallow renaming of the finch
    fields = ['color', 'size']
    # uses def get_absolute_url in models.py to redirect the put request
    # back to the the detail page of the cat just updated


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
    # redirect to finches_index path instead of same detail page


def finches_index(request):
    # tell the model to find all the rows in the finches table!
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })


def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.toys.all().values_list('id')
    # query the toys table for a the toys
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    # form object
    feeding_form = FeedingForm()
    print(finch.__dict__)

    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have

    })

# 'finches/<int:finch_id>/add_feeding/'


def add_feeding(request, finch_id):
    # process the form request form the client
    form = FeedingForm(request.POST)
    # request.POST is like req.body, its the contents of the form
    # validate the form
    if form.is_valid():
        # create an in memory instance (on django) of our data
        # to be added to psql, commit=False, don't save to db yet
        new_feeding = form.save(commit=False)
        # add the finch id to the new_feeding
        new_feeding.finch_id = finch_id
        new_feeding.save()  # adding a feeding row to the feeding table in psql
    return redirect('finch-detail', finch_id=finch_id)
    # finch_id is the name of the param, and the id from the finch url path


class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
