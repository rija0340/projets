# Generated by Django 2.1.7 on 2019-08-20 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_birth_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='birth_date',
            new_name='anniv',
        ),
    ]
