# Generated by Django 5.0.6 on 2024-05-18 16:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todolist", "0002_remove_task_tag_task_tags"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="tags",
            new_name="tag",
        ),
    ]
