from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Home</h1>')

def about(request):
  return render(request, 'about.html')


class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, classification, description, age):
    self.name = name
    self.classification = classification
    self.description = description
    self.age = age


finches = [
    Finch('George', 'Canary', 'loves to sing.', 2),
    Finch('Ben', 'House Finch', 'very old.', 12),
    Finch('Gunner', 'Hawfinch', 'Chunky.', 4),
    Finch('Beast', 'Brambling', 'Not Friendly.', 6)
]


def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})
