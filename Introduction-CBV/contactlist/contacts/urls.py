from django.urls import path
from . import views
from .views import ContactListView, ContactCreateView, ContactEditView, ContactDeleteView

# urlpatterns = [
#     path('', views.contact_list, name='contact_list'),
#     path('create/', views.contact_create, name='contact_create'),
#     path('edit/<int:contact_id>/', views.contact_edit, name='contact_edit'),
#     path('delete/<int:contact_id>/', views.contact_delete, name='contact_delete'),
# ]
urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('create/', ContactCreateView.as_view(), name='contact_create'),
    path('edit/<int:contact_id>/', ContactEditView.as_view(), name='contact_edit'),
    path('delete/<int:contact_id>/', ContactDeleteView.as_view(), name='contact_delete'),
]
