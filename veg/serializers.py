from rest_framework import serializers
from veg.models import ChooseCountry, Hotel, TypeVeg, RestrurantInfo, Gallery, RatingReviews, FoodOnlineOrder



class ChooseCountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ChooseCountry
        fields = ['country']

class TypeVegSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeVeg
        fields = ['type_veg']        

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ['title', 'image', 'discriptiion','user_id','choose_veg',]

class RestrurantInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestrurantInfo
        fields = ['hotal', 'mobile_number', 'overview', 'email', 'time',]

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ['hotal', 'gallery']

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingReviews
        fields = ['user_id', 'title', 'rating', 'reviews_discriptiion', 'hotal']

class FoodOnlineOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodOnlineOrder
        fields = ['user_id', 'order', 'title', 'discriptiion', 'price', 'food_image']


