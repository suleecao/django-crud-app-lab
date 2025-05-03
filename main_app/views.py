from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import OutfitForm
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shoe-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    contact_details = "you can reach us at admin@shoecollector.com"
    return render(request, 'about.html', {'contact': contact_details})

@login_required
def shoe_index(request):
    shoes = Shoe.objects.filter(user=request.user)
    return render(request, 'shoes/index.html', {'shoes': shoes})

@login_required
def shoe_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    outfit_form = OutfitForm()
    return render(request, 'shoes/detail.html', {
        'shoe': shoe, 
        'outfit_form': outfit_form
    })

class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    fields = ['brand', 'style', 'color', 'occasion']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShoeUpdate(LoginRequiredMixin, UpdateView):
    model = Shoe
    fields = ['brand', 'style', 'color', 'occasion']
    
class ShoeDelete(LoginRequiredMixin, DeleteView):
    model = Shoe
    success_url = '/shoes/'

@login_required
def add_outfit(request, shoe_id):
    form = OutfitForm(request.POST)
    if form.is_valid():
        new_outfit = form.save(commit=False)
        new_outfit.shoe_id = shoe_id
        new_outfit.save()
    return redirect('shoe-detail', shoe_id=shoe_id)