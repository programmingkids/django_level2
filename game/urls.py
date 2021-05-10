from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('player/list1', views.list1, name="list1"),
    path('player/list2', views.PlayerListView.as_view(), name="list2"),
    path('player/detail1/<int:pk>', views.detail1, name="detail1"),
    path('player/detail2/<int:pk>', views.PlayerDetailView.as_view(), name="detail2"),
]
