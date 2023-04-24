# Generated by Django 4.2 on 2023-04-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LeetcodeData",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("is_premium", models.BooleanField()),
                ("difficulty", models.CharField(max_length=6)),
                ("solution_link", models.CharField(max_length=100)),
                ("acceptance_rate", models.FloatField()),
                ("frequency", models.FloatField()),
                ("url", models.CharField(max_length=100)),
                ("discuss_count", models.IntegerField()),
                ("accepted", models.IntegerField()),
                ("submissions", models.CharField(max_length=4)),
                ("companies", models.TextField()),
                ("related_topics", models.CharField(max_length=1000)),
                ("likes", models.IntegerField()),
                ("dislikes", models.IntegerField()),
                ("rating", models.IntegerField()),
                ("asked_by_faang", models.BooleanField()),
                ("similar_questions", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]
