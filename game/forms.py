from django import forms


class Work01Form(forms.Form):
    name = forms.CharField(
        label = "名前",
        initial = "",
        widget=forms.TextInput(attrs={"class" : "form-control"}))
    grade = forms.ChoiceField(
        label = "学年",
        initial = "",
        choices = (
            ('1st', '1年'),
            ('2nd', '2年'),
            ('3rd', '3年'),
        ),
        widget=forms.Select(attrs={"class" : "form-control"}))
    language = forms.ChoiceField(
        label = "勉強してみたい言語",
        initial = "",
        choices = (
            ('English', '英語'),
            ('Spanish', 'スペイン語'),
            ('French', 'フランス語'),
            ('German', 'ドイツ語'),
        ),
        widget=forms.Select(attrs={"class" : "form-control"}))
    country = forms.ChoiceField(
        label="行きたい街",
        initial = "",
        choices = (
            ('LA', 'ロサンゼルス'),
            ('NewYork', 'ニューヨーク'),
            ('Sydney', 'シドニー'),
            ('London', 'ロンドン'),
            ('Moscow', 'モスクワ'),
            ('Cairo', 'カイロ'),
        ),
        widget=forms.RadioSelect(attrs={"class" : "form-control-custom"}))

