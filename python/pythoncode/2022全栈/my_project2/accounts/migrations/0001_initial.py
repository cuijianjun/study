# Generated by Django 3.0 on 2022-08-03 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('nickname', models.CharField(blank=True, max_length=256, null=True, verbose_name='用户昵称')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='用户头像')),
                ('status', models.SmallIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='用户状态')),
                ('is_super', models.BooleanField(default=False, verbose_name='是否为超级用户')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'accounts_user',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('real_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='真实姓名')),
                ('sex', models.SmallIntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], default=0, verbose_name='用户性别')),
                ('maxim', models.CharField(blank=True, max_length=128, null=True, verbose_name='用户格言')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='用户地址')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.User', verbose_name='关联用户')),
            ],
            options={
                'db_table': 'accounts_user_profile',
            },
        ),
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='用户名')),
                ('login_type', models.CharField(max_length=128, verbose_name='账号平台')),
                ('ip', models.CharField(default='', max_length=32, verbose_name='IP地址')),
                ('ua', models.CharField(default='', max_length=128, verbose_name='登录来源')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登录时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_history_list', to='accounts.User', verbose_name='关联的用户')),
            ],
            options={
                'db_table': 'accounts_login_history',
                'ordering': ['-created_at'],
            },
        ),
    ]
