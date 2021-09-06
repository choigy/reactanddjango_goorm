from rest_framework import routers
from .views import TestViewSet


router = routers.SimpleRouter()
router.register(r'tests', TestViewSet)
urlpatterns = router.urls
