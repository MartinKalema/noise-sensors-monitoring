# Generated by Django 3.2.6 on 2022-03-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0016_auto_20220208_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='category',
            field=models.CharField(choices=[('A', 'Category A: hospital, home for the aged, higher learning institute, public library'), ('B', 'Category B: Residential buildings'), ('C', 'Category C: Mixed residential (with some commercial and entertainment)'), ('D', 'Category D: Residential + industry or small-scale production + commerce'), ('E', 'Category E: Industrial')], default='E', max_length=50),
        ),
    ]
