from django.shortcuts import render

from .models import Player

from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy


# Create your views here.
def list1(request) :
    # 全レコード取り出し
    object_list = Player.objects.all()
    
    context = {
        "title" : "プレイヤー一覧",
        "message" : "プレイヤーを一覧で表示します",
        "object_list" : object_list
    }
    return render(request, "game/work01.html", context)


class PlayerListView(ListView):
    # モデル名
    model = Player
    # テンプレートファイル名のパス
    template_name = "game/work01.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プレイヤー一覧"
        context["message"] = "プレイヤー一覧を表示します"
        return context


