from django.urls import path
from api_rest.views import TenisListCreate, TenisRetrieveUpdateDestroy

urlpatterns = [
    path('', TenisListCreate.as_view(), name='tenis-list-create'),  
    path('admin/', TenisListCreate.as_view(), name='tenis-list-create'),
    path('admin/<int:pk>/', TenisRetrieveUpdateDestroy.as_view(), name='tenis-detail'),
]
