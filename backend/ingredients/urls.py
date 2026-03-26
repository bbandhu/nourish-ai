from django.urls import path
from . import views

urlpatterns = [
    path('', views.IngredientListView.as_view(), name='ingredient-list'),
    path('<slug:slug>/', views.IngredientDetailView.as_view(), name='ingredient-detail'),
]
