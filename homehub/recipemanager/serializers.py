"""
This file contains the serializers for the 'recipemanager' app within the 'HomeHub' project.
The purpose of these serializers is to convert the Recipe and Ingredient model instances
into JSON format for the API and to deserialize JSON data back into model instances.
"""

# Import the serializers module from the Django REST framework
from rest_framework import serializers

# Import the Ingredient, Recipe, and RecipeIngredient models from the 'recipemanager' app
from homehub.recipemanager.models import Ingredient, Recipe, RecipeIngredient

# Define a serializer for the Ingredient model
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

# Define a serializer for the RecipeIngredient model
class RecipeIngredientSerializer(serializers.ModelSerializer):
    # Use the IngredientSerializer to serialize the related Ingredient instance
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'unit', 'quantity')

# Define a serializer for the Recipe model
class RecipeSerializer(serializers.ModelSerializer):
    # Use the RecipeIngredientSerializer to serialize the related RecipeIngredient instances for a Recipe
    ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'instructions', 'prep_time', 'cook_time', 'servings', 'ingredients')
