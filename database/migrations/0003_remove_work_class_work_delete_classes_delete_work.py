# Generated by Django 4.2.3 on 2023-07-05 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rename_class_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='class_work',
        ),
        migrations.DeleteModel(
            name='Classes',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
