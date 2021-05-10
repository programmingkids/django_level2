from django import forms
from .models import Player

class PlayerForm (forms.ModelForm) :
    JOB_CHOICES = [('','選択してください')] + list(Player.JOB_CHOICES)
    
    class Meta:
        model = Player
        fields = ['name','hp','mp','job','birthday']
    
    name = forms.CharField(
        label = "名前",
        widget = forms.TextInput(attrs={"class" : "form-control"}))
        
    hp = forms.IntegerField(
        label = "HP",
        widget = forms.NumberInput(attrs={"class" : "form-control"}))
        
    mp = forms.IntegerField(
        label = "MP",
        widget = forms.NumberInput(attrs={"class" : "form-control"}))
        
    job = forms.ChoiceField(
        label = "職業",
        choices = JOB_CHOICES,
        widget = forms.Select(attrs={"class" : "form-control"}))
        
    birthday = forms.DateField(
        label = "誕生日",
        widget = forms.TextInput(attrs={"class" : "form-control", "type":"date"}))
