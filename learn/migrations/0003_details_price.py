# Generated by Django 3.0.5 on 2020-05-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20200512_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='Price',
            field=models.IntegerField(default=0),
        ),
    ]
