# Generated by Django 2.0.2 on 2018-03-13 05:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_room', '0006_users_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditType',
            fields=[
                ('au_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('audit_type', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
