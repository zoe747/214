# Generated by Django 3.2.5 on 2021-07-09 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friends',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_user', to=settings.AUTH_USER_MODEL),
        ),
    ]