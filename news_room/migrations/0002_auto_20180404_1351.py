# Generated by Django 2.0.2 on 2018-04-04 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_room', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infographassociation',
            options={'ordering': ['date_created'], 'verbose_name': 'InfographAssociation', 'verbose_name_plural': 'InfographAssociations'},
        ),
    ]