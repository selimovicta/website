# Generated by Django 3.2.9 on 2022-05-20 08:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220519_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
