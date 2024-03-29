# Generated by Django 5.0.1 on 2024-01-31 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortUrl",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                (
                    "short_url",
                    models.CharField(db_index=True, max_length=20, unique=True),
                ),
                ("original_url", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
