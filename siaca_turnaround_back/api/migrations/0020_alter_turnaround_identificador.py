# Generated by Django 4.2.2 on 2023-09-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_turnaround_fecha_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnaround',
            name='identificador',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
