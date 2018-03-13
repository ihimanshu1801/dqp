# Generated by Django 2.0.2 on 2018-03-13 05:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_room', '0009_associationtype_userassociations'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('as_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('app_set', models.CharField(max_length=50)),
                ('app_val', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'AppSetting',
                'verbose_name_plural': 'AppSettings',
            },
        ),
        migrations.CreateModel(
            name='UserAudit',
            fields=[
                ('uau_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('u_id', models.PositiveIntegerField()),
                ('au_id', models.PositiveIntegerField()),
                ('element_id', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('audittype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_room.AuditType')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_room.Users')),
            ],
        ),
    ]
