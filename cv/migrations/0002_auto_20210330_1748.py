# Generated by Django 3.1.7 on 2021-03-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra_Curri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curri_year', models.ImageField(upload_to='')),
                ('curri_desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='lang',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.PositiveBigIntegerField(),
        ),
    ]