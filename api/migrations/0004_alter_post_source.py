# Generated by Django 3.2 on 2022-10-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.CharField(default='<django.db.models.fields.related.ForeignKey>', max_length=255),
        ),
    ]
