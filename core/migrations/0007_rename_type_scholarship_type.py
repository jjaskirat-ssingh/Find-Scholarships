# Generated by Django 4.0.3 on 2022-03-07 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_type_scholarship_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship',
            old_name='Type',
            new_name='type',
        ),
    ]
