# Generated by Django 4.2.7 on 2023-12-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgfeedApp', '0008_rename_message_id_like_like_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='message_id',
            new_name='comment_id',
        ),
    ]
