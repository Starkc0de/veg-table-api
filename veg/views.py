from .models import ChooseCountry, Hotel, TypeVeg, RestrurantInfo, Gallery, RatingReviews, FoodOnlineOrder,BookTable
from .serializers import ChooseCountrySerializer, HotelSerializer, TypeVegSerializer, RestrurantInfoSerializer, GallerySerializer, RatingSerializer, FoodOnlineOrderSerializer, BookTableSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings


# Create your views here.

class ChooseCountryView(generics.ListAPIView):
    queryset = ChooseCountry.objects.all()
    serializer_class = ChooseCountrySerializer

    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class HotelView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = CustomPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title']


class TypeVegView(generics.ListAPIView):
    queryset = TypeVeg.objects.all()
    serializer_class = TypeVegSerializer 

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  

class RestrurantViewView(generics.ListAPIView):
    queryset = RestrurantInfo.objects.all()
    serializer_class = RestrurantInfoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GalleryView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RatingView(generics.ListCreateAPIView):
    queryset = RatingReviews.objects.all()
    serializer_class = RatingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FoodOnlineOrderView(generics.ListAPIView):
    queryset = FoodOnlineOrder.objects.all()
    serializer_class = FoodOnlineOrderSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class SearchView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'discriptiion']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'discriptiion']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BookTableView(generics.ListCreateAPIView):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializer
    pagination_class = CustomPagination        

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
