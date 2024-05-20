'''from django.shortcuts import render
from .models import Medecin

def liste_medecins(request):
    medecins = Medecin.objects.all()
    return render(request, 'medecins/liste_medecins.html', {'medecins': medecins})
from rest_framework import generics

from rest_framework import generics
from .models import Medecin
from .serializers import MedecinSerializer

class MedecinListCreate(generics.ListCreateAPIView):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class MedecinRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer'''

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import Medecin
from .serializers import MedecinSerializer
from .forms import MedecinForm

# API Views
class MedecinListCreate(generics.ListCreateAPIView):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class MedecinRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

# Template Views
def medecin_list(request):
    medecins = Medecin.objects.all()
    return render(request, 'medecins/medecin_list.html', {'medecins': medecins})

def medecin_detail(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    return render(request, 'medecins/medecin_detail.html', {'medecin': medecin})

def medecin_create(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medecin_list')
    else:
        form = MedecinForm()
    return render(request, 'medecins/medecin_form.html', {'form': form})

def medecin_update(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            return redirect('medecin_list')
    else:
        form = MedecinForm(instance=medecin)
    return render(request, 'medecins/medecin_form.html', {'form': form})

def medecin_delete(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == 'POST':
        medecin.delete()
        return redirect('medecin_list')
    return render(request, 'medecins/medecin_confirm_delete.html', {'medecin': medecin})

def search_medecin(request):
    if request.method == 'GET':
        form = MedecinForm(request.GET)
        if form.is_valid():
            search_name = form.cleaned_data['search_name']
            medecins = Medecin.objects.filter(nom__icontains=search_name)
            return render(request, 'search_results.html', {'medecins': medecins, 'form': form})
    else:
        form = MedecinForm()
    return render(request, 'search_medecin.html', {'form': form})