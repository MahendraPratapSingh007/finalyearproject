# Generated by Django 2.2 on 2020-08-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0003_auto_20200807_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='dob',
            field=models.DateField(),
        ),
    ]
