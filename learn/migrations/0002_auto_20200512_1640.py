# Generated by Django 3.0.5 on 2020-05-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='details',
            name='Flute_type',
            field=models.CharField(max_length=20),
        ),
    ]
