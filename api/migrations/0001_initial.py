# Generated by Django 3.1.4 on 2021-02-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('temperature', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('rainfall', models.IntegerField()),
                ('population_density', models.IntegerField()),
                ('region_size', models.IntegerField()),
            ],
        ),
    ]
