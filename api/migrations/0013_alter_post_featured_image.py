# Generated by Django 3.2 on 2022-10-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='/uploads/post_images/news-800x500-1.jpg', upload_to='uploads/post_images/'),
        ),
    ]
