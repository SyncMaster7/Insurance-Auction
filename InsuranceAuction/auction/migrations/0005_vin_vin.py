# Generated by Django 4.0.3 on 2022-04-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_alter_motorcycle_color_alter_otheritem_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vin',
            name='vin',
            field=models.CharField(default='WDB2110281A301836', max_length=17),
        ),
    ]
