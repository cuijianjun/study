# Generated by Django 3.0 on 2022-07-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=64, null=True, verbose_name='用户的邮箱'),
        ),
    ]
