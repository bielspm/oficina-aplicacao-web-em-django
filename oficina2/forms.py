from .models import Orcamento
from django import forms

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = '__all__'