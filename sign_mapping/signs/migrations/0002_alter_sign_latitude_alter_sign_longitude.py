# Generated by Django 5.1.5 on 2025-01-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign',
            name='latitude',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
        migrations.AlterField(
            model_name='sign',
            name='longitude',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
    ]
