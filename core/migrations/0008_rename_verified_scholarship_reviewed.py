# Generated by Django 4.0.3 on 2022-03-07 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_type_scholarship_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship',
            old_name='verified',
            new_name='reviewed',
        ),
    ]
