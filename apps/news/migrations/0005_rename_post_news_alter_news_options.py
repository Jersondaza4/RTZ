# Generated by Django 4.2.5 on 2024-02-14 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='News',
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
    ]
