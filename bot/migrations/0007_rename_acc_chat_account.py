# Generated by Django 4.2.4 on 2023-09-06 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_alter_account_user_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='acc',
            new_name='account',
        ),
    ]
