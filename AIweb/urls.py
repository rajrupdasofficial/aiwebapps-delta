from django.urls import path
from .views import *

app_home='AIweb'

urlpatterns=[
    path('sales/',SalesListView.as_view(),name='list'),
    path('',home_view,name="Test_url"),
    path('sales/<pk>/',SaleDetailView.as_view(),name="detail"),
]