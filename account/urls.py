from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customers', views.CustomerView)
router.register('accounts', views.AccountView)
router.register('transfers', views.TransferView)

urlpatterns = [
    path('', include(router.urls)),
    path('history/<str:id>/', views.TransferHistory),
    path('balance/<str:id>/', views.balance),
]