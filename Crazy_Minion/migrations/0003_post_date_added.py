# Generated by Django 2.2.5 on 2020-06-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crazy_Minion', '0002_auto_20200609_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]