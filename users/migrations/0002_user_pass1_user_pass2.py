# Generated by Django 5.1.4 on 2024-12-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pass1',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pass2',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
