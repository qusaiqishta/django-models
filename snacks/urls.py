from django.urls import path
from .views import SnackListView , SnackDetailView ,HomeView

urlpatterns=[
    path('',HomeView.as_view(),name='base'),
    path('list',SnackListView.as_view(),name='snack_list'),
    path('list/<int:pk>',SnackDetailView.as_view(),name='snack_details')
]