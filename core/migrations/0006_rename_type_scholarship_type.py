# Generated by Django 4.0.3 on 2022-03-07 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_type_scholarship_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship',
            old_name='type',
            new_name='Type',
        ),
    ]
