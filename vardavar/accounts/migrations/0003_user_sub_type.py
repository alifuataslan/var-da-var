# Generated by Django 4.0.5 on 2022-06-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_yemekler'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sub_type',
            field=models.PositiveBigIntegerField(choices=[(1, 'Üye'), (2, 'RestoranSahibi'), (3, 'SuperUser')], default=1),
        ),
    ]
