from django.urls import path, include
from . import views
from rest_framework import routers

## TEST
# router = routers.DefaultRouter()
# router.register('customers', views.CustomerView, basename='customers')
# router.register('accounts', views.AccountView, basename='accounts')
# router.register('transfers', views.TransferView, basename='transfers')
#
# urlpatterns = [
#     path('', include((router.urls,'account'))),
#     path('history/<str:id>/', views.TransferHistory),
#     path('balance/<str:id>/', views.balance),
# ]

router = routers.DefaultRouter()
router.register('customers', views.CustomerView)
router.register('accounts', views.AccountView)
router.register('transfers', views.TransferView)

urlpatterns = [
    path('', include((router.urls))),
    path('accounts/<str:id>/history', views.TransferHistory),
]