# Generated by Django 3.2.9 on 2021-11-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='desc',
            field=models.CharField(max_length=200),
        ),
    ]
