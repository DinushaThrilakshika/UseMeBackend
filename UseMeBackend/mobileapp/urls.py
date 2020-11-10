from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mobileapp',views.CustomerView)
router.register('mobileapp',views.ShopView)
router.register('mobileapp',views.DpersonView)

urlpatterns = [
    path('',include(router.urls))
]