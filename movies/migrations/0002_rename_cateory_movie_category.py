# Generated by Django 4.1.2 on 2023-02-01 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='cateory',
            new_name='category',
        ),
    ]
