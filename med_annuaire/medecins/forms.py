from django import forms
from .models import Medecin

class MedecinForm(forms.ModelForm):
    # Champ de recherche pour le nom du médecin
    search_name = forms.CharField(label='Rechercher par nom', required=False)

    class Meta:
        model = Medecin
        fields = '__all__'



#Cela facilite la création d'interfaces utilisateur pour
# la création ou la modification d'instances de ce modèle.