# Generated by Django 4.1.7 on 2023-07-02 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api_user", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="biology",
            new_name="biography",
        ),
    ]
