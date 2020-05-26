# Generated by Django 3.0.5 on 2020-04-14 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artwork', '0002_art_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='artist', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]