# Generated by Django 3.2.7 on 2021-09-21 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watchlist_app', '0005_auto_20210921_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
