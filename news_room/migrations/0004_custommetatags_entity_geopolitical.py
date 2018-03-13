# Generated by Django 2.0.2 on 2018-03-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_room', '0003_mastertopics_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomMetaTags',
            fields=[
                ('mtg_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('metatag', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('entity_code', models.CharField(max_length=50)),
                ('entity_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GeoPolitical',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('gp_code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
