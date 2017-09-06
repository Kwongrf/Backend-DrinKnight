from django.contrib import admin

# Register your models here.
from drinknight.models import User
from drinknight.models import DrinkData
admin.site.register(User)
admin.site.register(DrinkData)