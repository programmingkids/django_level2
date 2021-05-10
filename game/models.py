from django.db import models

# Create your models here.
class Player (models.Model):
    """
    name text
    hp int
    mp int
    job select
    birthday date
    """
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
