# Generated by Django 4.2.2 on 2023-07-14 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_alter_turnaround_fecha_fin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario_turnaround',
            name='fk_usuario',
        ),
        migrations.AddField(
            model_name='usuario_turnaround',
            name='fk_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
