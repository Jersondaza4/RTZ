# Generated by Django 4.2.5 on 2024-03-25 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_is_admin_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='facebook'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='instagram'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='twitter'),
        ),
        migrations.AddField(
            model_name='user',
            name='web',
            field=models.URLField(blank=True, null=True, verbose_name='web'),
        ),
    ]
