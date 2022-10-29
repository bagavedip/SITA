# Generated by Django 4.0 on 2022-10-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sita', '0027_alter_extractor_itsm_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit_itsm',
            name='total_data',
            field=models.IntegerField(help_text='total_data', null=True, verbose_name='total_data'),
        ),
        migrations.AddField(
            model_name='audit_itsm_stg',
            name='total_data',
            field=models.IntegerField(help_text='total_data', null=True, verbose_name='total_data'),
        ),
        migrations.AddField(
            model_name='audit_siem',
            name='total_data',
            field=models.IntegerField(help_text='total_data', null=True, verbose_name='total_data'),
        ),
        migrations.AddField(
            model_name='audit_siem_stg',
            name='total_data',
            field=models.IntegerField(help_text='total_data', null=True, verbose_name='total_data'),
        ),
        migrations.AddField(
            model_name='audit_soar_extractor',
            name='total_data',
            field=models.IntegerField(help_text='total_data', null=True, verbose_name='total_data'),
        ),
        migrations.AddField(
            model_name='audit_soar_stg',
            name='total_data',
            field=models.IntegerField(help_text='total_data', null=True, verbose_name='total_data'),
        ),
    ]