from django.db import models


class Grid(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ['id']


class Mine(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField()
    grid = models.ForeignKey(Grid, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class Square(models.Model):
    id = models.AutoField(primary_key=True)
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
    revealed = models.BooleanField()
    flagged = models.BooleanField()
    value = models.IntegerField()

    grid = models.ForeignKey(Grid, on_delete=models.CASCADE)
    mine = models.OneToOneField(
        Mine,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['id']