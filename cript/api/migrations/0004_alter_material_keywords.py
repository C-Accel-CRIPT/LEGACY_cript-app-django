# Generated by Django 3.2.5 on 2021-07-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210729_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='api.Keyword'),
        ),
    ]
