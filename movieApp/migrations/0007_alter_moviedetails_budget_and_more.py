# Generated by Django 5.2.1 on 2025-06-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0006_alter_moviedetails_budget_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedetails',
            name='budget',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moviedetails',
            name='collection',
            field=models.IntegerField(),
        ),
    ]
