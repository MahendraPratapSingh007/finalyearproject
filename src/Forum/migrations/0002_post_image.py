# Generated by Django 2.2 on 2020-04-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
