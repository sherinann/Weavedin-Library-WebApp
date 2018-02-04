# Generated by Django 2.0.1 on 2018-02-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0006_auto_20180203_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='author',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('id', models.AutoField(primary_key=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('pob', models.CharField(max_length=40)),
            ],
        ),
    ]

