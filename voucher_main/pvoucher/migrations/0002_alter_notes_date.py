# Generated by Django 4.1 on 2023-03-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvoucher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
