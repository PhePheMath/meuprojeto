from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Enquetes
from .forms import EnqueteForm

def boasvindas(request):
    return render(request, 'bemvindo.html')

def criar_enquete(request):
    if request.method == 'POST':
        form = EnqueteForm(request.POST)
        if form.is_valid():
            enquete = form.save()
            return HttpResponseRedirect(reverse('mostrar_enquete', kwargs={'enquete_id': enquete.pk}))
    return render(request, 'enquete_form.html', {'form': EnqueteForm()})

def show_enquete(request, enquete_id):
    enquete = Enquetes.objects.get(id=enquete_id)
    return render(request, 'enquetes.html', {'enquete':enquete})
