from .models import ChooseCountry, Hotel, TypeVeg, RestrurantInfo, Gallery, RatingReviews, FoodOnlineOrder
from .serializers import ChooseCountrySerializer, HotelSerializer, TypeVegSerializer, RestrurantInfoSerializer, GallerySerializer, RatingSerializer, FoodOnlineOrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ChooseCountryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated ]
    queryset = ChooseCountry.objects.all()
    serializer_class = ChooseCountrySerializer

class HotelView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class TypeVegView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = TypeVeg.objects.all()
    serializer_class = TypeVegSerializer   

class RestrurantViewView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = RestrurantInfo.objects.all()
    serializer_class = RestrurantInfoSerializer

class GalleryView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class RatingView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = RatingReviews.objects.all()
    serializer_class = RatingSerializer

class FoodOnlineOrderView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = FoodOnlineOrder.objects.all()
    serializer_class = FoodOnlineOrderSerializer
    pagination_class = CustomPagination

