from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'author',
                  'description', 'prep_time', 'cook_time']
        read_only_field = ['id']

    def create(self, validated_data):
        recipe = Recipe.objects.create(**validated_data)
        return recipe

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
