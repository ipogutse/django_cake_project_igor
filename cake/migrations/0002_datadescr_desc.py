# Generated by Django 4.1.7 on 2023-02-27 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datadescr',
            name='desc',
            field=models.TextField(default='igor'),
            preserve_default=False,
        ),
    ]