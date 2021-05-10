from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from .models import Player
from .forms import PlayerForm


# Create your views here.
def list1(request) :
    # 全レコードを取得
    object_list = Player.objects.all()
    
    context = {
        "title" : "プレイヤー一覧",
        "message" : "プレイヤーを一覧で表示します",
        "object_list" : object_list
    }
    return render(request, "game/list1.html", context)


class PlayerListView(ListView):
    # モデル名
    model = Player
    # テンプレートファイル名のパス
    template_name = "game/list2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プレイヤー一覧"
        context["message"] = "プレイヤー一覧を表示します"
        return context


def detail1(request, pk) :
    # 指定されたレコードを取得
    object = Player.objects.get(id=pk)
    
    context = {
        "title" : "プレイヤー詳細表示",
        "message" : "1件のプレイヤーを表示します",
        "object" : object
    }
    return render(request, "game/detail1.html", context)


class PlayerDetailView(DetailView) :
    # モデル名
    model = Player
    # テンプレートファイル名の指定
    template_name = "game/detail2.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プレイヤー詳細表示"
        context["message"] = "1件のプレイヤーを表示します"
        return context
    

def create1(request) :
    context = {
        "title" : "プレイヤー新規作成",
        "message" : "プレイヤーを作成します",
        "form" : PlayerForm()
    }
    
    # POSTの場合
    if request.method == "POST":
        # Playerオブジェクト作成
        player = Player()
        # リクエストデータと結合
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid() :
            # エラーがない場合、新規登録
            form.save()
            # 一覧画面へリダイレクト
            return redirect("game:list1")
        else :
            # エラーがある場合、登録画面を再度表示
            context['form'] = form
    return render(request, "game/create1.html", context)


class PlayerCreateView(CreateView) :
    # モデル名
    model = Player
    # フォームクラス名
    form_class = PlayerForm
    # 登録成功時のリダイレクト先URL指定
    success_url = reverse_lazy("game:list2")
    # テンプレートファイル名の指定
    template_name = "game/create2.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プレイヤー新規作成"
        context["message"] = "プレイヤーを作成します"
        return context


def update1(request, pk):
    # 指定されたレコードを取得
    object =Player.objects.get(id=pk)
    
    context = {
        "title" : "プレイヤー更新",
        "message" : "プレイヤーを更新します",
        "object" : object,
        "form" : PlayerForm(instance=object),
    }
    
    # POSTの場合
    if request.method == "POST":
        # リクエストデータと結合
        form = PlayerForm(request.POST, instance=object)
        
        if form.is_valid() :
            # エラーがない場合、新規登録
            form.save()
            # 一覧画面へリダイレクト
            return redirect("game:list1")
        else :
            context["form"] = form
    return render(request, "game/update1.html", context)


class PlayerUpdateView(UpdateView) :
    # モデル名
    model = Player
    # フォームクラス名
    form_class = PlayerForm
    # 登録成功時のリダイレクト先URL指定
    success_url = reverse_lazy("game:list2")
    # テンプレートファイル名の指定
    template_name = "game/update2.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プレイヤー更新"
        context["message"] = "プレイヤーを更新します"
        return context


def delete1(request, pk) :
    # 指定されたレコードを取得
    object = Player.objects.get(id=pk)
    # 指定されたオブジェクトを削除
    object.delete()
    # 一覧画面へリダイレクト
    return redirect("game:list1")


class PlayerDeleteView(DeleteView) :
    # モデル名
    model = Player
    # 削除成功時のリダイレクト先URL指定
    success_url = reverse_lazy("game:list2")

    def get(self, *args, **kwargs):
        # プライマリーキーの取得
        pk = self.kwargs.get("pk")
        # 指定されたレコードを取得
        object = Player.objects.get(id=pk)
        # 指定されたオブジェクトを削除
        object.delete()
        # 一覧画面へリダイレクト
        return redirect(self.success_url)

