from django.shortcuts import render
from .form import ExamploModelForm  # Certifique-se de importar o formulário corretamente

def index(request):
    form = ExamploModelForm()
    return render(request, 'exemplo/formularios/formulario1.html', {'form': form})
