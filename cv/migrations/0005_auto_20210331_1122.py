# Generated by Django 3.1.7 on 2021-03-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20210331_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='grades',
            field=models.FloatField(),
        ),
    ]
