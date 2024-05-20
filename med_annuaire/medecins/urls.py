'''from django.urls import path
from .views import MedecinListCreate, MedecinRetrieveUpdateDestroy

urlpatterns = [
    path('medecins/', MedecinListCreate.as_view(), name='medecin-list-create'),
    path('medecins/<int:pk>/', MedecinRetrieveUpdateDestroy.as_view(), name='medecin-detail'),
]'''

from django.urls import path
from .views import (
    medecin_list,
    medecin_detail,
    medecin_create,
    medecin_update,
    medecin_delete,
    search_medecin,
    MedecinListCreate,
    MedecinRetrieveUpdateDestroy
    
)

urlpatterns = [
    path('api/medecins/', MedecinListCreate.as_view(), name='medecin-list-create'),
    path('api/medecins/<int:pk>/', MedecinRetrieveUpdateDestroy.as_view(), name='medecin-detail'),
    path('medecins/', medecin_list, name='medecin_list'),
    path('medecins/<int:pk>/', medecin_detail, name='medecin_detail'),
    path('medecins/create/', medecin_create, name='medecin_create'),
    path('medecins/<int:pk>/edit/', medecin_update, name='medecin_update'),
    path('medecins/<int:pk>/delete/', medecin_delete, name='medecin_delete'),
    path('search/', search_medecin, name='search_medecin'),
]

