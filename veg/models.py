from email.policy import default
from django.db import models
from django_countries.fields import CountryField

from account.models import User


class ChooseCountry(models.Model):
    country = CountryField(default = 'IN')

    def __str__(self):
        return str(self.country)

    class Meta:
        verbose_name_plural = "ChooseCountry"  # display table name for admin
        db_table = 'ChooseCountry' 

class TypeVeg(models.Model):
    type_veg = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.type_veg)

    class Meta:
        verbose_name_plural = "TypeVeg"  # display table name for admin
        db_table = 'TypeVeg' 

class Hotel(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    choose_veg = models.ForeignKey(TypeVeg, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.FileField(upload_to='media/hotal', null=True, blank=True)
    discriptiion = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Hotel"  # display table name for admin
        db_table = 'Hotel' 

class RestrurantInfo(models.Model):
    hotal = models.ForeignKey(Hotel, on_delete=models.CASCADE,null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    overview = models.TextField( null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return str(self.overview)

    class Meta:
        verbose_name_plural = "RestrurantInfo"  # display table name for admin
        db_table = 'RestrurantInfo' 

class Gallery(models.Model):
    hotal = models.ForeignKey(Hotel, on_delete=models.CASCADE,null=True, blank=True)
    gallery = models.FileField(upload_to='media/gallery', null=True, blank=True)

    def __str__(self):
        return str(self.gallery)

    class Meta:
        verbose_name_plural = "Gallery"  # display table name for admin
        db_table = 'Gallery'

class RatingReviews(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    hotal = models.ForeignKey(Hotel, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    reviews_discriptiion = models.TextField(null=True, blank=True) 

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "RatingReviews"  # display table name for admin
        db_table = 'RatingReviews'

class FoodOnlineOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    order = models.ForeignKey(Hotel, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    discriptiion = models.TextField(null=True, blank=True) 
    price = models.IntegerField(null=True, blank=True)
    food_image = models.ImageField(upload_to='media/food', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "FoodOnlineOrder"  # display table name for admin
        db_table = 'FoodOnlineOrder'                                                                 