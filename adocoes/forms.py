from django import forms
from .models import Adocao,InteresseAdocao

class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = ["solicitante", "animal", "status"]
        labels = {
            "solicitante": "Solicitante",
            "animal": "Animal",
            "status": "Status da Adoção:",
        }
        widgets = {
            "solicitante": forms.Select(attrs={"class": "form-control"}),
            "animal": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
class InteresseAdocaoForm(forms.ModelForm):
    class Meta:
        model = InteresseAdocao
        fields = ['animal', 'mensagem']
