from django.urls import path
from . import trip_views
from . import user_views

urlpatterns = [
    path('trips/', trip_views.TripList.as_view()),
    path('users/', user_views.UserList.as_view())
    # path('trips/<int:id>/', trip_views.get_trip),
]