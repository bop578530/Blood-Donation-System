# Generated by Django 5.0.3 on 2024-03-26 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='register',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
