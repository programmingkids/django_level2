# Generated by Django 3.1 on 2021-05-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hp', models.IntegerField(default=0)),
                ('type', models.IntegerField(choices=[(1, '炎属性'), (2, '水属性'), (3, '雷属性'), (4, '光属性'), (5, '闇属性')])),
                ('attack', models.IntegerField(default=0)),
            ],
        ),
    ]
