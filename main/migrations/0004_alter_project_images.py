# Generated by Django 4.0 on 2022-10-20 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_project_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ImageField(blank=True, default='./static/img/download.png', null=True, upload_to='images/'),
        ),
    ]
