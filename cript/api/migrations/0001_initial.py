# Generated by Django 3.2.5 on 2021-07-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('material_type', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=1000)),
            ],
        ),
    ]
