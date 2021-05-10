from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('player/list1', views.player_list1, name="player_list1"),
    path('player/list2', views.PlayerListView.as_view(), name="player_list2"),
    path('player/detail1/<int:pk>', views.player_detail1, name="player_detail1"),
    path('player/detail2/<int:pk>', views.PlayerDetailView.as_view(), name="player_detail2"),
    path('player/create1', views.player_create1, name="player_create1"),
    path('player/create2', views.PlayerCreateView.as_view(), name="player_create2"),
    path('player/update1/<int:pk>', views.player_update1, name="player_update1"),
    path('player/update2/<int:pk>', views.PlayerUpdateView.as_view(), name="player_update2"),
    path('player/delete1/<int:pk>', views.player_delete1, name="player_delete1"),
    path('player/delete2/<int:pk>', views.PlayerDeleteView.as_view(), name="player_delete2"),
]
