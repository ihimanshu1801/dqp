# Generated by Django 2.0.2 on 2018-03-13 05:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_room', '0005_infographassociation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('login', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('usertype_id', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gp_id', models.PositiveIntegerField()),
                ('status_id', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('appstatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_room.AppStatus')),
                ('geopolitical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_room.GeoPolitical')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('usertype_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('usertype', models.CharField(max_length=50)),
            ],
        ),
    ]