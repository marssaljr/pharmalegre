# Generated by Django 4.0.1 on 2022-01-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pills',
            name='buyday',
        ),
        migrations.RemoveField(
            model_name='pills',
            name='buytime',
        ),
        migrations.DeleteModel(
            name='BuyDay',
        ),
        migrations.DeleteModel(
            name='BuyTime',
        ),
    ]
