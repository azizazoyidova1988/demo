# Generated by Django 3.2.4 on 2021-06-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='image',
        ),
        migrations.AddField(
            model_name='about',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='about',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
