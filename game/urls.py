from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('player/list1', views.list1, name="list1"),
    path('player/list2', views.PlayerListView.as_view(), name="list2")
]
