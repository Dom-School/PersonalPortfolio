# Generated by Django 2.2.3 on 2019-07-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190726_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.FilePathField(blank=True, null=True, path='/img'),
        ),
    ]