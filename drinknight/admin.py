from django.contrib import admin

# Register your models here.
from drinknight.models import User
from drinknight.models import DrinkData
from drinknight.models import DayDrinkData
from drinknight.models import MonthDrinkData
from drinknight.models import YearDrinkData

class DrinkDataAdmin(admin.ModelAdmin):
    list_display = ('account','dose','time')
class DayDrinkDataAdmin(admin.ModelAdmin):
    list_display = ('account','volume_dose','date')
class MonthDrinkDataAdmin(admin.ModelAdmin):
    list_display = ('account','volume_dose','month')
class YearDrinkDataAdmin(admin.ModelAdmin):
    list_display = ('account','volume_dose','year')

admin.site.register(User)
admin.site.register(DrinkData,DrinkDataAdmin)
admin.site.register(DayDrinkData,DayDrinkDataAdmin)
admin.site.register(MonthDrinkData,MonthDrinkDataAdmin)
admin.site.register(YearDrinkData,YearDrinkDataAdmin)