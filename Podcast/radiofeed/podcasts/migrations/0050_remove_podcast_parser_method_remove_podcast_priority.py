# Generated by Django 4.2.2 on 2023-06-10 20:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("podcasts", "0049_podcast_parser_method"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="podcast",
            name="parser_method",
        ),
        migrations.RemoveField(
            model_name="podcast",
            name="priority",
        ),
    ]