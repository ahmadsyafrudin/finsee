# Generated by Django 4.1.2 on 2022-10-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
