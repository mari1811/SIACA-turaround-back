# Generated by Django 4.2.2 on 2023-10-04 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_alter_maquinaria_historial_hora_fin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquinaria_historial',
            name='fk_turnaround',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.turnaround'),
        ),
        migrations.DeleteModel(
            name='maquinaria_turnaround',
        ),
    ]
