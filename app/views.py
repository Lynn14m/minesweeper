from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

from app.models import Grid, Square
from app.serializers import GridSerializer, SquareSerializer
from app.game_logic import init_grid

class FrontEnd(View):
    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {})


class GridList(APIView):
    """
    List all Grids or create new Grid
    """

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        grids = Grid.objects.all()

        serializer = GridSerializer(grids, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = GridSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GridDetail(APIView):
    """
    Retrieve, update or delete Grid
    """

    def get_object(self, id):
        try:
            return Grid.objects.get(id=id)
        except:
            raise Http404

    @method_decorator(csrf_exempt)
    def get(self, request, pk, format=None):
        grid = self.get_object(pk)
        serializer = GridSerializer(grid)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        grid = self.get_object(pk)
        serializer = GridSerializer(grid, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        grid = self.get_object(pk)
        grid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SquareList(APIView):
    """
    List all Squares or create new Squares
    """

    @method_decorator(csrf_exempt)
    def get(self, request, format=None):
        squares = Square.objects.all()

        serializer = SquareSerializer(squares, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = SquareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SquareDetail(APIView):
    """
    Retrieve, update or delete Square
    """
    def get_object(self, id):
        try:
            return Square.objects.get(id=id)
        except:
            raise Http404

    @method_decorator(csrf_exempt)
    def get(self, request):
        square = Square.objects.get(row=request.headers['row'], column=request.headers['column'], grid=request.headers['grid'])
        serializer = SquareSerializer(square)
        return Response(serializer.data)

    def put(self, request, pk):
        square = self.get_object(pk)
        serializer = SquareSerializer(square, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        square = self.get_object(pk)
        square.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InitialiseSquares(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        grid = Grid(rows_count=request.data['rowsCount'], columns_count=request.data['columnsCount'], mines_count=request.data['mineCount'])
        grid.save()
        grid_array = init_grid(grid)

        for i in range(len(grid_array)):
            for j in range(len(grid_array)):
                value = grid_array[i][j]
                square = Square(row=i, column=j, value=value, grid=grid)
                square.save()
        serializer = GridSerializer(grid)
        return Response(serializer.data, status=status.HTTP_200_OK)
