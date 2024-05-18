# Generated by Django 5.0.6 on 2024-05-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.CharField(max_length=255)),
                ("datetime", models.DateTimeField()),
                ("deadline", models.DateTimeField()),
                ("is_completed", models.BooleanField(default=False)),
                ("tag", models.ManyToManyField(to="todolist.tag")),
            ],
            options={
                "ordering": ("datetime",),
            },
        ),
    ]
