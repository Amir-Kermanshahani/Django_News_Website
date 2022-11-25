# Generated by Django 3.2 on 2022-10-24 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=10)),
                ('category', models.CharField(blank=True, default='', max_length=100)),
                ('tag', models.CharField(blank=True, default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField(blank=True, default='')),
                ('source', models.CharField(default=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL), max_length=255)),
                ('featured_image', models.ImageField(height_field=500, null=True, upload_to='D:\\Python\\News_Website\\media', width_field=800)),
                ('image1', models.ImageField(height_field=500, null=True, upload_to='D:\\Python\\News_Website\\media', width_field=800)),
                ('image2', models.ImageField(height_field=500, null=True, upload_to='D:\\Python\\News_Website\\media', width_field=800)),
                ('views_number', models.PositiveIntegerField(null=True)),
                ('comments_number', models.PositiveIntegerField(null=True)),
                ('released', models.BooleanField(blank=True, default=False)),
                ('featured', models.BooleanField(blank=True, default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
