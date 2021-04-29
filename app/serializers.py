from rest_framework import serializers
from app.models import Grid, Mine, Square


class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = ['id', ]


class MineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mine
        fields = ['id', 'grid', 'value']


class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Square
        fields = ['id', 'row', 'column', 'revealed', 'flagged', 'value', 'grid', 'mine']