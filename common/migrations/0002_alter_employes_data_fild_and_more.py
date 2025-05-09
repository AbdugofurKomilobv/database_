# Generated by Django 5.1.7 on 2025-03-18 18:38

import common.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employes',
            name='data_fild',
            field=models.FileField(upload_to='uplods/', validators=[common.models.Employes.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='employes',
            name='fk_departamen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departament', to='common.departament'),
        ),
        migrations.AlterField(
            model_name='employes',
            name='fk_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='common.region'),
        ),
    ]
