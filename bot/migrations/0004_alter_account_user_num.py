# Generated by Django 4.2.4 on 2023-09-05 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_remove_chat_user_account_user_num_chat_acc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_num',
            field=models.IntegerField(null=True),
        ),
    ]
