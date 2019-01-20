# Generated by Django 2.1.2 on 2018-12-16 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avatar',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avatars', to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='avatar',
            name='recommended_by_staff',
            field=models.BooleanField(default=False),
        ),
    ]