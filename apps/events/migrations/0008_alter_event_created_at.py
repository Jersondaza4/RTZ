# Generated by Django 4.2.5 on 2024-02-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
