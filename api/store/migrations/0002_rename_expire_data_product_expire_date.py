# Generated by Django 3.2.23 on 2024-02-15 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='expire_data',
            new_name='expire_date',
        ),
    ]
