# Generated by Django 2.0 on 2017-12-24 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditate', '0003_auto_20171223_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
