from django.shortcuts import render_to_response, get_object_or_404
from models import Recipe, Ingredient

# Create your views here.
def home(request):
  recipes=Recipe.objects.all()
  ingredients=Ingredient.objects.all()
  context = {'ingredients_list':ingredients, 'recipes_list':recipes, 'days':["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]}
  return render_to_response('food/index.html', context)
  