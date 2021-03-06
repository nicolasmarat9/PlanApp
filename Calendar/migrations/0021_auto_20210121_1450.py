# Generated by Django 3.1 on 2021-01-21 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Calendar', '0020_auto_20210121_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_1',
            field=models.IntegerField(blank=True, default='26'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_10',
            field=models.IntegerField(blank=True, default='5'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_11',
            field=models.IntegerField(blank=True, default='6'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_12',
            field=models.IntegerField(blank=True, default='7'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_13',
            field=models.IntegerField(blank=True, default='8'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_14',
            field=models.IntegerField(blank=True, default='9'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_15',
            field=models.IntegerField(blank=True, default='10'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_16',
            field=models.IntegerField(blank=True, default='11'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_17',
            field=models.IntegerField(blank=True, default='12'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_18',
            field=models.IntegerField(blank=True, default='13'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_19',
            field=models.IntegerField(blank=True, default='14'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_2',
            field=models.IntegerField(blank=True, default='27'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_20',
            field=models.IntegerField(blank=True, default='15'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_21',
            field=models.IntegerField(blank=True, default='16'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_22',
            field=models.IntegerField(blank=True, default='17'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_23',
            field=models.IntegerField(blank=True, default='18'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_24',
            field=models.IntegerField(blank=True, default='19'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_25',
            field=models.IntegerField(blank=True, default='20'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_26',
            field=models.IntegerField(blank=True, default='21'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_27',
            field=models.IntegerField(blank=True, default='22'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_28',
            field=models.IntegerField(blank=True, default='23'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_29',
            field=models.IntegerField(blank=True, default='24'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_3',
            field=models.IntegerField(blank=True, default='28'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_30',
            field=models.IntegerField(blank=True, default='25'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_31',
            field=models.IntegerField(blank=True, default='26'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_32',
            field=models.IntegerField(blank=True, default='27'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_33',
            field=models.IntegerField(blank=True, default='28'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_34',
            field=models.IntegerField(blank=True, default='29'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_35',
            field=models.IntegerField(blank=True, default='30'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_36',
            field=models.IntegerField(blank=True, default='31'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_37',
            field=models.IntegerField(blank=True, default='1'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_38',
            field=models.IntegerField(blank=True, default='2'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_39',
            field=models.IntegerField(blank=True, default='3'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_4',
            field=models.IntegerField(blank=True, default='29'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_40',
            field=models.IntegerField(blank=True, default='4'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_41',
            field=models.IntegerField(blank=True, default='5'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_42',
            field=models.IntegerField(blank=True, default='6'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_5',
            field=models.IntegerField(default='30'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_6',
            field=models.IntegerField(blank=True, default='1'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_7',
            field=models.IntegerField(blank=True, default='2'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_8',
            field=models.IntegerField(blank=True, default='3'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='day_9',
            field=models.IntegerField(blank=True, default='4'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_1',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_2',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_3',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_37',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_38',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_39',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_4',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_40',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_41',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_42',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='slug_day_5',
            field=models.SlugField(blank=True, default='off'),
        ),
        migrations.AlterField(
            model_name='e_2021_may',
            name='title',
            field=models.CharField(blank=True, default='May 2021', max_length=50),
        ),
        migrations.CreateModel(
            name='B_2020_January',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='January 2020', max_length=50)),
                ('day_1', models.IntegerField(default='30')),
                ('slug_day_1', models.SlugField(default='off')),
                ('color1', models.CharField(default='off', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
