from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('player/list1', views.list1, name="list1"),
    path('player/list2', views.PlayerListView.as_view(), name="list2"),
    path('player/detail1/<int:pk>', views.detail1, name="detail1"),
    path('player/detail2/<int:pk>', views.PlayerDetailView.as_view(), name="detail2"),
    path('player/create1', views.create1, name="create1"),
    path('player/create2', views.PlayerCreateView.as_view(), name="create2"),
    path('player/update1/<int:pk>', views.update1, name="update1"),
    path('player/update2/<int:pk>', views.PlayerUpdateView.as_view(), name="update2"),
]
