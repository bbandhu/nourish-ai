from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AgentQuery
from .agents.nutrition_agent import run_nutrition_decoder
from .agents.ingredient_agent import run_ingredient_story
from .agents.recipe_agent import run_recipe_breakdown


class NutritionDecoderView(APIView):
    def post(self, request):
        ingredients = request.data.get('ingredients', [])
        if not ingredients:
            return Response({'error': 'No ingredients provided'}, status=400)
        try:
            result = run_nutrition_decoder(ingredients)
            AgentQuery.objects.create(
                agent='nutrition_decoder',
                input_text=', '.join(ingredients),
                output_text=str(result),
                success=True
            )
            return Response(result)
        except Exception as e:
            AgentQuery.objects.create(
                agent='nutrition_decoder',
                input_text=', '.join(ingredients),
                success=False,
                error_message=str(e)
            )
            return Response({'error': str(e)}, status=500)


class IngredientStoryView(APIView):
    def post(self, request):
        ingredient = request.data.get('ingredient', '')
        if not ingredient:
            return Response({'error': 'No ingredient provided'}, status=400)
        try:
            result = run_ingredient_story(ingredient)
            AgentQuery.objects.create(
                agent='ingredient_story',
                input_text=ingredient,
                output_text=str(result),
                success=True
            )
            return Response(result)
        except Exception as e:
            AgentQuery.objects.create(
                agent='ingredient_story',
                input_text=ingredient,
                success=False,
                error_message=str(e)
            )
            return Response({'error': str(e)}, status=500)


class RecipeBreakdownView(APIView):
    def post(self, request):
        recipe_name = request.data.get('recipe_name', '')
        ingredients = request.data.get('ingredients', [])
        if not ingredients:
            return Response({'error': 'No ingredients provided'}, status=400)
        try:
            result = run_recipe_breakdown(recipe_name, ingredients)
            AgentQuery.objects.create(
                agent='recipe_breakdown',
                input_text=f"{recipe_name}: {', '.join(ingredients)}",
                output_text=str(result),
                success=True
            )
            return Response(result)
        except Exception as e:
            AgentQuery.objects.create(
                agent='recipe_breakdown',
                input_text=recipe_name,
                success=False,
                error_message=str(e)
            )
            return Response({'error': str(e)}, status=500)
