# Generated by Django 5.0.6 on 2024-05-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todolist", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="tag",
        ),
        migrations.AddField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(to="todolist.tag"),
        ),
    ]
