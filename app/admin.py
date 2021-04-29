from django.contrib import admin
from app.models import Grid, Mine, Square


# Register your models here.
class GridAdmin(admin.ModelAdmin):
    list_display = ['id']


class MineAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'grid')


class SquareAdmin(admin.ModelAdmin):
    list_display = ('id', 'row', 'column', 'revealed', 'flagged', 'value', 'grid', 'mine')


admin.site.register(Grid, GridAdmin)
admin.site.register(Mine, MineAdmin)
admin.site.register(Square, SquareAdmin)
