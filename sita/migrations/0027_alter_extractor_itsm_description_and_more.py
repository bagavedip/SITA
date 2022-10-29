# Generated by Django 4.0 on 2022-10-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sita', '0026_audit_itsm_no_dump_data_audit_itsm_stg_no_dump_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractor_itsm',
            name='description',
            field=models.CharField(help_text='Description', max_length=100000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='extractor_itsm',
            name='resolution_content',
            field=models.CharField(help_text='Resolution Content', max_length=100000, null=True, verbose_name='resolution_content'),
        ),
    ]