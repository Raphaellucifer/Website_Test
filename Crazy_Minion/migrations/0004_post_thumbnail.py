# Generated by Django 2.2.5 on 2020-06-25 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Crazy_Minion', '0003_post_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='thumbnails'),
            preserve_default=False,
        ),
    ]
