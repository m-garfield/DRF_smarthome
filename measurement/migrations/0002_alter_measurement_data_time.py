# Generated by Django 4.1.7 on 2023-03-26 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='data_time',
            field=models.DateTimeField(auto_now=True, max_length=50),
        ),
    ]