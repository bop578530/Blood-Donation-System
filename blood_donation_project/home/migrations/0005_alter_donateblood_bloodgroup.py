# Generated by Django 5.0.3 on 2024-03-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateblood',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B-', 'B-'), ('B-', 'B+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O-', 'O-'), ('O+', 'O+')], max_length=50),
        ),
    ]
