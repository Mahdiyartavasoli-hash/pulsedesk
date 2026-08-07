from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, TicketViewSet, TicketMessageViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'messages', TicketMessageViewSet, basename='ticketmessage')

urlpatterns = router.urls
