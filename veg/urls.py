from django.urls import path
from .views import ChooseCountryView, HotelView, TypeVegView, RestrurantViewView, GalleryView, RatingView, FoodOnlineOrderView, SearchView, BookTableView


urlpatterns = [
    
    path('country/', ChooseCountryView.as_view(), name='country'),
    path('hotal/', HotelView.as_view(), name='hotal'),
    path('type-veg/', TypeVegView.as_view(), name='type-veg'),
    path('restrurent-info/', RestrurantViewView.as_view(), name='restrurent-info'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('rating/', RatingView.as_view(), name='rating'),
    path('food-online/', FoodOnlineOrderView.as_view(), name='food-online'),
    path('search/', SearchView.as_view(), name='search'),
    path('book-table/', BookTableView.as_view(), name='book-table'),

]
