# Generated by Django 4.1.7 on 2023-06-13 06:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api_project", "0004_transaction_full_name_transaction_is_anonymous_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="user_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
