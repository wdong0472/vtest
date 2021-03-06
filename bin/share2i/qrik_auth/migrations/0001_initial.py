# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 22:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('qrik_key', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qrik_version', models.IntegerField(default=1, verbose_name='\u7248\u672c\u53f7')),
                ('qrik_code', models.CharField(default='', max_length=200, verbose_name='\u7f16\u7801')),
                ('qrik_name', models.CharField(default='', max_length=200, verbose_name='\u540d\u79f0')),
                ('qrik_value', models.CharField(default='0', max_length=200, verbose_name='\u503c')),
                ('qrik_order_no', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u53f7')),
                ('qrik_enabled', models.BooleanField(default=True, verbose_name='\u542f\u7528\u6807\u8bc6')),
                ('qrik_del_flag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u8bc6')),
                ('qrik_stamp', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('qrik_update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('qrik_summary', models.TextField(blank=True, verbose_name='\u63cf\u8ff0')),
                ('icon', models.URLField(verbose_name='\u529f\u80fd\u56fe\u6807')),
            ],
            options={
                'get_latest_by': 'qrik_update_time',
                'ordering': ['-qrik_order_no'],
                'abstract': False,
                'verbose_name_plural': '\u529f\u80fd\u64cd\u4f5c',
                'verbose_name': '\u529f\u80fd\u64cd\u4f5c',
            },
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('qrik_key', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qrik_version', models.IntegerField(default=1, verbose_name='\u7248\u672c\u53f7')),
                ('qrik_code', models.CharField(default='', max_length=200, verbose_name='\u7f16\u7801')),
                ('qrik_name', models.CharField(default='', max_length=200, verbose_name='\u540d\u79f0')),
                ('qrik_value', models.CharField(default='0', max_length=200, verbose_name='\u503c')),
                ('qrik_order_no', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u53f7')),
                ('qrik_enabled', models.BooleanField(default=True, verbose_name='\u542f\u7528\u6807\u8bc6')),
                ('qrik_del_flag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u8bc6')),
                ('qrik_stamp', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('qrik_update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('qrik_summary', models.TextField(blank=True, verbose_name='\u63cf\u8ff0')),
                ('icon', models.URLField(verbose_name='\u529f\u80fd\u56fe\u6807')),
                ('qrik_creater', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='qrik_auth_app_related_creater', related_query_name='qrik_auth_app_related_creater_query', to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u4eba')),
                ('qrik_updater', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='qrik_auth_app_related_updater', related_query_name='qrik_auth_app_relates_updater_query', to=settings.AUTH_USER_MODEL, verbose_name='\u4fee\u6539\u4eba')),
            ],
            options={
                'get_latest_by': 'qrik_update_time',
                'ordering': ['-qrik_order_no'],
                'abstract': False,
                'verbose_name_plural': '\u529f\u80fd\u6a21\u5757',
                'verbose_name': '\u529f\u80fd\u6a21\u5757',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('qrik_key', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qrik_version', models.IntegerField(default=1, verbose_name='\u7248\u672c\u53f7')),
                ('qrik_code', models.CharField(default='', max_length=200, verbose_name='\u7f16\u7801')),
                ('qrik_name', models.CharField(default='', max_length=200, verbose_name='\u540d\u79f0')),
                ('qrik_value', models.CharField(default='0', max_length=200, verbose_name='\u503c')),
                ('qrik_order_no', models.IntegerField(default=0, verbose_name='\u6392\u5e8f\u53f7')),
                ('qrik_enabled', models.BooleanField(default=True, verbose_name='\u542f\u7528\u6807\u8bc6')),
                ('qrik_del_flag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u8bc6')),
                ('qrik_stamp', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('qrik_update_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('qrik_summary', models.TextField(blank=True, verbose_name='\u63cf\u8ff0')),
                ('icon', models.URLField(verbose_name='\u529f\u80fd\u56fe\u6807')),
                ('app', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='qrik_auth.App', verbose_name='\u529f\u80fd\u6a21\u5757')),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='\u7528\u6237\u7ec4')),
                ('qrik_creater', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='qrik_auth_menu_related_creater', related_query_name='qrik_auth_menu_related_creater_query', to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u4eba')),
                ('qrik_updater', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='qrik_auth_menu_related_updater', related_query_name='qrik_auth_menu_relates_updater_query', to=settings.AUTH_USER_MODEL, verbose_name='\u4fee\u6539\u4eba')),
            ],
            options={
                'get_latest_by': 'qrik_update_time',
                'ordering': ['-qrik_order_no'],
                'abstract': False,
                'verbose_name_plural': '\u529f\u80fd\u83dc\u5355',
                'verbose_name': '\u529f\u80fd\u83dc\u5355',
            },
        ),
        migrations.AddField(
            model_name='action',
            name='menu',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='qrik_auth.Menu', verbose_name='\u529f\u80fd\u83dc\u5355'),
        ),
        migrations.AddField(
            model_name='action',
            name='qrik_creater',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='qrik_auth_action_related_creater', related_query_name='qrik_auth_action_related_creater_query', to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u4eba'),
        ),
        migrations.AddField(
            model_name='action',
            name='qrik_updater',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='qrik_auth_action_related_updater', related_query_name='qrik_auth_action_relates_updater_query', to=settings.AUTH_USER_MODEL, verbose_name='\u4fee\u6539\u4eba'),
        ),
    ]
