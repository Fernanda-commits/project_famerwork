from django.shortcuts import render, redirect
from .models import Persona 
from .form import PersonaForms

#create your views here.

def registerUser(request):
    if request.method == 'POST':
        form = PersonaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarUsuarios')
    else:
        form = PersonaForms()
        
    return render(request,'registroUsuario.html', {'form': form}) 

def listarUsuarios(request):
    personas = Persona.objects.all()
    return render(request, "listarUsuarios.html", {"personas": personas})