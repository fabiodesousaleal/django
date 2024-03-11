from django import forms
from .models import ExemploModel

class ExamploModelForm(forms.ModelForm):
    class Meta:
        model = ExemploModel
        fields = '__all__'  # Ou especifique os campos que deseja incluir no formulário
