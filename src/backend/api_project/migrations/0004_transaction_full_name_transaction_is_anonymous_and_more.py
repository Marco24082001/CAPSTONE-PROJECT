# Generated by Django 4.1.7 on 2023-06-12 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_project', '0003_alter_project_id_alter_transaction_id_alter_type_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='full_name',
            field=models.CharField(default='Anonymous', max_length=255),
        ),
        migrations.AddField(
            model_name='transaction',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
