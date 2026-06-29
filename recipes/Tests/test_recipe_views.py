from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))