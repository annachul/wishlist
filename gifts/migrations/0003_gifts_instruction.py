# Generated by Django 3.2.8 on 2021-11-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0002_gifts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gifts',
            name='instruction',
            field=models.TextField(null=True),
        ),
    ]
