# Generated by Django 4.1.3 on 2024-04-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YemekSepeti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siparis',
            name='sip_id',
            field=models.IntegerField(default=0),
        ),
    ]
