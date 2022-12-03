from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

#Cat models thats connected to the database
from .models import Cat

# temp add Cats class
# getting rid of this because it exists in models.py
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

#     def __str__(self):
#         return f"{self.name}"

# cats = [
#     Cat('Rufus', 'tabbycat', 'crazy cat', 103),
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Cat('Raven', 'black tripod', '3 legged cat', 4)
# ] 


class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/cats/' + str(self.object.pk))

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'


# Create your views here.
def index(request):
    cats = list(Cat.objects.all())
    return render(request, 'index.html', { 'cats': cats })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def cats_index(request):
    cats = list(Cat.objects.all())
    return render(request, 'cats/index.html', { 'cats': cats })

def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)

    return render(request, 'cats/show.html', { 'cat': cat })