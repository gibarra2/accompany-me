from django.urls import path
from . import trip_views
from . import user_views

urlpatterns = [
    path('trips/', trip_views.TripList.as_view()),
    path('users/', user_views.UserList.as_view()),
    path('users/<int:pk>/', user_views.UserDetail.as_view()),
    path('users/filter=<str:email>/', user_views.UserDetail.as_view())
]