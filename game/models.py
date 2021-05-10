from django.db import models

# Create your models here.
class Player (models.Model):
    JOB_CHOICES = (
        (1, '勇者'),
        (2, '魔法使い'),
        (3, '戦士'),
        (4, '賢者'),
        (5, '遊び人'),
    )
    
    name = models.CharField(
        max_length=100
    )
    hp = models.IntegerField(
        default=0
    )
    mp = models.IntegerField(
        default=0
    )
    job = models.IntegerField(
        choices=JOB_CHOICES
    )
    birthday = models.DateField(
    )
    
    def __str__(self):
        s = "<Player " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            "HP=" + str(self.hp) + " " + \
            "MP=" + str(self.mp) + " " + \
            "職業=" + self.get_job_display() + " " + \
            "誕生日=" + str(self.birthday) + " " + \
            ">"
        return s


class Enemy (models.Model):
    TYPE_CHOICES = (
        (1, '炎属性'),
        (2, '水属性'),
        (3, '雷属性'),
        (4, '光属性'),
        (5, '闇属性'),
    )
    
    name = models.CharField(
        max_length=100
    )
    hp = models.IntegerField(
        default=0
    )
    type = models.IntegerField(
        choices=TYPE_CHOICES
    )
    attack = models.IntegerField(
        default=0
    )
    
    def __str__(self):
        s = "<Enemy " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            "HP=" + str(self.hp) + " " + \
            "タイプ=" + self.get_type_display() + " " + \
            "攻撃力=" + str(self.attack) + " " + \
            ">"
        return s
