# Generated by Django 3.1 on 2021-01-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0003_a_2021_january_color14'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_dailyplan',
            name='color1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='m_dailyplan',
            name='color2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='m_dailyplan',
            name='color3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='m_dailyplan',
            name='color4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='m_dailyplan',
            name='color5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='m_dailyplan',
            name='color6',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='m_dailyplan',
            name='color7',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='m_dailyplan',
            name='color8',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
