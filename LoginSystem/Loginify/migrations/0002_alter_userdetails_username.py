# Generated by Django 5.1.5 on 2025-01-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Loginify", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetails",
            name="username",
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
