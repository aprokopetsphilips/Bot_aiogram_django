# Generated by Django 4.2.4 on 2023-09-05 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_alter_account_user_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='acc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.account'),
        ),
    ]