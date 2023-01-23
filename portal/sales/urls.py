from django.urls import path

from .views import (
    HomePageView,
    MyListView,
    TkpDetailView,
    TkpCreateView,
    TkpUpdateView,
    TkpDeleteView,
    about,
)

urlpatterns = [
    path('tkp/about/', about, name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('tkp/mylist/', MyListView.as_view(), name='my_list'),
    path('tkp/new/', TkpCreateView.as_view(), name='tkp_add'),
    path('tkp/<int:pk>/', TkpDetailView.as_view(), name='tkp_detail'),
    path('tkp/<int:pk>/edit/', TkpUpdateView.as_view(), name='tkp_edit'),
    path('tkp/<int:pk>/delete/', TkpDeleteView.as_view(), name='tkp_delete'),
    ]
