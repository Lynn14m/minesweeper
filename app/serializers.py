from rest_framework import serializers
from app.models import Grid, Square


class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = ['id', 'rows_count', 'columns_count', 'mines_count']


class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Square
        fields = ['id', 'grid', 'row', 'column', 'revealed', 'clickable', 'flagged', 'is_known', 'is_safe',
                  'is_mine', 'value']
