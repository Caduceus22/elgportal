from django.urls import path

from .views import (
    HomePageView,
    MyListView,
    TkpCreateView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tkp/mylist/', MyListView.as_view(), name='my_list'),
    path('tkp/new/', TkpCreateView.as_view(), name='tkp_add'),
    ]
