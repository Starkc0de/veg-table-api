from django.contrib import admin
from veg.models import ChooseCountry, Hotel, TypeVeg, RestrurantInfo, Gallery, RatingReviews, FoodOnlineOrder, BookTable
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class ChooseCountryAdmin(ModelAdmin):
    list_display = ["country"]
admin.site.register(ChooseCountry, ChooseCountryAdmin)

class TypeVegAdmin(ModelAdmin):
    list_display = ["type_veg"]
admin.site.register(TypeVeg, TypeVegAdmin)

class HotelAdmin(ModelAdmin):
    list_display = ['title', 'image', 'discriptiion','user_id','choose_veg',]
admin.site.register(Hotel, HotelAdmin)

class RestrurantInfoAdmin(ModelAdmin):
    list_display = ['hotal', 'mobile_number', 'overview', 'email', 'time',]
admin.site.register(RestrurantInfo, RestrurantInfoAdmin)

class GalleryAdmin(ModelAdmin):
    list_display = ['hotal', 'gallery']
admin.site.register(Gallery, GalleryAdmin)

class RatingAdmin(ModelAdmin):
    list_display = ['user_id', 'title', 'rating', 'reviews_discriptiion', 'hotal']
admin.site.register(RatingReviews, RatingAdmin)

class FoodOnlineOrderAdmin(ModelAdmin):
    list_display = ['user_id', 'order', 'title', 'discriptiion', 'price', 'food_image']
admin.site.register(FoodOnlineOrder, FoodOnlineOrderAdmin)

class BookTableAdmin(ModelAdmin):
    list_display = ['book_id', 'hotel', 'people', 'name', 'email', 'date_booking', 'preferred_table', 'phone_number']
admin.site.register(BookTable, BookTableAdmin)
