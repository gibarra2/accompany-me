from django.urls import path
from .views import trip_views, user_views, place_views

urlpatterns = [
    path('users/', user_views.UserList.as_view()),
    path('users/<int:pk>/', user_views.UserDetail.as_view()),
    path('users/<str:email>/', user_views.UserDetail.as_view()), 
    path('users/<int:pk>/trips/', user_views.UserTrips.as_view()), 
    path('trips/<int:pk>/', trip_views.TripDetail.as_view()),
    path('trips/<int:pk>/users/', trip_views.TripUsers.as_view()), 
    path('trips/<int:pk>/places/', trip_views.TripPlaces.as_view()),
    path('places/<int:pk>/', place_views.PlaceDetail.as_view()),
]