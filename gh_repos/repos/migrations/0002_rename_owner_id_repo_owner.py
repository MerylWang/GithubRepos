# Generated by Django 4.1.7 on 2023-03-17 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repo',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
