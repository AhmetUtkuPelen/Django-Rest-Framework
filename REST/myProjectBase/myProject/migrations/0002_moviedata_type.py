# Generated by Django 5.0.2 on 2024-04-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
