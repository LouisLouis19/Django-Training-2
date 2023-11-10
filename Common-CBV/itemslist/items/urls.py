from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/create/', ItemCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
