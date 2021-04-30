from django.contrib import admin
from app.models import Grid, Square


# Register your models here.
class GridAdmin(admin.ModelAdmin):
    list_display = ['id', 'rows_count', 'columns_count', 'mines_count']


class SquareAdmin(admin.ModelAdmin):
    list_display = ('id', 'grid', 'row', 'column', 'revealed', 'clickable', 'flagged', 'is_known', 'is_safe', 'is_mine',
                    'value')


admin.site.register(Grid, GridAdmin)
admin.site.register(Square, SquareAdmin)
