# Generated by Django 3.2.6 on 2022-02-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0015_auto_20220208_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='division',
            field=models.CharField(blank=True, default='N/A', max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='parish',
            field=models.CharField(blank=True, default='N/A', max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='village',
            field=models.CharField(blank=True, default='N/A', max_length=200),
        ),
    ]