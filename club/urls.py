from rest_framework import routers
from .views import ClubModelViewSet

club_router = routers.SimpleRouter()
club_router.register(r'clubs', ClubModelViewSet)

