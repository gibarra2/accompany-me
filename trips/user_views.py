from rest_framework.generics import ListCreateAPIView
from profiles.models import DummyUser
from trips.serializers import UserSerializer

class UserList(ListCreateAPIView):
    queryset = DummyUser.objects.all()
    serializer_class = UserSerializer