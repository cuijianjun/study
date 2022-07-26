# Generated by Django 3.0 on 2022-07-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220726_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('nickname', models.CharField(max_length=64, verbose_name='昵称')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
