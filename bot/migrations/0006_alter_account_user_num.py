# Generated by Django 4.2.4 on 2023-09-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_alter_chat_acc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]