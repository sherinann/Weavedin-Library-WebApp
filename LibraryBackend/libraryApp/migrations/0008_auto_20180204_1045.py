# Generated by Django 2.0.1 on 2018-02-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0007_auto_20180204_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2),
        ),
        migrations.AlterField(
            model_name='author',
            name='pob',
            field=models.CharField(default='india', max_length=20),
        ),
    ]