from django.contrib import admin
from .models import PizzaSize, Pizza

admin.site.register(PizzaSize)
# admin.site.register(Pizza)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    """Категории"""
    search_fields = ('title',)
    list_display = ('id', 'title')
    list_display_links = ('title',)
    list_filter = ('title',)
