# Generated by Django 4.2.9 on 2024-03-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tires', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.CharField(max_length=10),
        ),
    ]
