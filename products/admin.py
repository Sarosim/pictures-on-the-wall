from django.contrib import admin
from .models import Category, Product, Artist, Technology, Rating, Badge, Size, Format, Room, Hashtag

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Artist)
admin.site.register(Technology)
admin.site.register(Rating)
admin.site.register(Badge)
admin.site.register(Size)
admin.site.register(Format)
admin.site.register(Room)
admin.site.register(Hashtag)