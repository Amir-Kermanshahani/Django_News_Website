# Generated by Django 3.2 on 2022-10-25 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_remove_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
