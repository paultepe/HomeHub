"""
This file defines the models for the 'recipemanager' app within the 'HomeHub' project.
It contains three main models: Ingredient, Recipe, and RecipeIngredient.

Ingredient: Represents an individual ingredient, storing its name.
Recipe: Represents a recipe, storing its title, description, instructions, 
        prep_time, cook_time, servings, and ingredients.
RecipeIngredient: Represents the relationship between a Recipe and its Ingredients,
                  storing the quantity and unit of each ingredient in a recipe.
"""

from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity} {self.unit}"
