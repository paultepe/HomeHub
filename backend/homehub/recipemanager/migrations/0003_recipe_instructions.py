# Generated by Django 4.1.7 on 2023-03-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipemanager', '0002_ingredient_remove_recipe_instructions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
