# Generated by Django 3.1.7 on 2021-03-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointGeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat_coord', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon_coord', models.DecimalField(decimal_places=6, max_digits=9)),
                ('geometry_type', models.CharField(default='', max_length=5)),
                ('feature_type', models.CharField(default='', max_length=7)),
                ('baloon_content', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
