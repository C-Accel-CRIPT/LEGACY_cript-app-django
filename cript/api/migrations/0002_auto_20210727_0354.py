# Generated by Django 3.2.5 on 2021-07-27 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='material_type',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='material',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
