# Generated by Django 4.1.3 on 2022-11-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)]),
        ),
    ]
