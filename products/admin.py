from django.contrib import admin
from .models import Category, Product, Artist, Technologies, Rating, Badge, Size, Format

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Artist)
admin.site.register(Technologies)
admin.site.register(Rating)
admin.site.register(Badge)
admin.site.register(Size)
admin.site.register(Format)
