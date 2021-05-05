from django.db import models


class Grid(models.Model):
    id = models.AutoField(primary_key=True)

    rows_count = models.IntegerField(default=0)
    columns_count = models.IntegerField(default=0)
    mines_count = models.IntegerField(default=0)  # Use the mine count to determine the number of mines to be created

    class Meta:
        ordering = ['id']


class Square(models.Model):
    id = models.AutoField(primary_key=True)

    grid = models.ForeignKey(Grid, on_delete=models.CASCADE)
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()

    revealed = models.BooleanField(default=False)
    clickable = models.BooleanField(default=True)
    flagged = models.BooleanField(default=False)

    is_known = models.BooleanField(default=False)  # Can value of square be deduced based on revealed information?
    is_safe = models.BooleanField(
        default=False)  # Should only be set to true after revealed information, take care of first click of game
    is_mine = models.BooleanField(
        default=False)  # When squares/grid are instantiated it's filled with 0 values before adding mines and values > 0

    value = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']
