# Generated by Django 3.1.3 on 2023-07-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='indicator',
            field=models.BooleanField(default=False),
        ),
    ]
