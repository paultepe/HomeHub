"""
This file defines the URL patterns for the 'recipemanager' app within the 'HomeHub' project.
The purpose of these URL patterns is to map the various API endpoints to their corresponding views,
providing a clear structure for accessing the recipe and ingredient resources.
"""

from django.urls import path
from homehub.recipemanager import views

urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredient-detail'),
]
