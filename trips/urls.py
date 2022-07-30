from django.urls import path
from . import trip_views
from . import user_views

urlpatterns = [
    path('users/', user_views.UserList.as_view()),
    path('users/<int:pk>/', user_views.UserDetail.as_view()),
    path('users/<str:email>/', user_views.UserDetail.as_view()), 
    path('users/<int:pk>/trips/', user_views.UserTrips.as_view()), 
    path('trips/<int:pk>/', trip_views.delete_trip),
    path('trips/<int:pk>/users/', trip_views.TripUsers.as_view())
]