# Generated by Django 4.0 on 2022-10-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sita', '0018_alter_stg_soar_ticketids'),
    ]

    operations = [
        migrations.AddField(
            model_name='stg_itsm',
            name='soar_id',
            field=models.IntegerField(help_text='Soar id', null=True, verbose_name='soar_id'),
        ),
    ]
