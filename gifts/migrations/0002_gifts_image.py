# Generated by Django 3.2.8 on 2021-11-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gifts',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
