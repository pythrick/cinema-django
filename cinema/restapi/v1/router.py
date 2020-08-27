from rest_framework import routers
from .viewsets import reservas


router = routers.DefaultRouter()
router.register(r'salas', reservas.SalasViewSet, basename="salas")
# router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
