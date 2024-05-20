from rest_framework import serializers
from .models import Medecin

class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = '__all__'



#utilisé pour convertir des instances du modèle Medecin en représentations JSON et vice versa,
# facilitant ainsi la création d'une API web à l'aide de Django REST Framework.