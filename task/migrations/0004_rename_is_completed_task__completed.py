# Generated by Django 5.0.6 on 2024-06-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_is_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_completed',
            new_name='_completed',
        ),
    ]