# Generated by Django 4.0 on 2022-10-14 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sita', '0023_alter_extractor_itsm_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='stg_siem',
            name='asset_type',
            field=models.CharField(help_text='Asset_type', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='extractor_siem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='created at', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='extractor_soar',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='created at', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='stg_itsm',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='created at', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='stg_siem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='created at', verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='stg_soar',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='created at', verbose_name='created at'),
        ),
    ]
