# Generated by Django 4.0.2 on 2022-02-22 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestopantry_app', '0002_user_useringredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password_hash',
            field=models.CharField(max_length=64),
        ),
    ]