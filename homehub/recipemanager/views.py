"""
This file contains the views for the 'recipemanager' app within the 'HomeHub' project.
The purpose of these views is to handle API requests for recipe and ingredient resources,
providing the necessary CRUD operations for managing these resources.
"""

# Import the generics module from the Django REST framework
from rest_framework import generics

# Import the Recipe and Ingredient models from the 'recipemanager' app
from homehub.recipemanager.models import Recipe, Ingredient

# Import the serializers for Recipe and Ingredient models
from homehub.recipemanager.serializers import RecipeSerializer, IngredientSerializer

# Define a view for listing and creating recipes
class RecipeList(generics.ListCreateAPIView):
    # Set the queryset to include all Recipe instances
    queryset = Recipe.objects.all()
    # Set the serializer class to the RecipeSerializer
    serializer_class = RecipeSerializer

# Define a view for retrieving, updating, and deleting a specific recipe
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    # Set the queryset to include all Recipe instances
    queryset = Recipe.objects.all()
    # Set the serializer class to the RecipeSerializer
    serializer_class = RecipeSerializer

# Define a view for listing and creating ingredients
class IngredientList(generics.ListCreateAPIView):
    # Set the queryset to include all Ingredient instances
    queryset = Ingredient.objects.all()
    # Set the serializer class to the IngredientSerializer
    serializer_class = IngredientSerializer

# Define a view for retrieving, updating, and deleting a specific ingredient
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    # Set the queryset to include all Ingredient instances
    queryset = Ingredient.objects.all()
    # Set the serializer class to the IngredientSerializer
    serializer_class = IngredientSerializer
