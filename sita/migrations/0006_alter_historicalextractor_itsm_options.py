# Generated by Django 4.0 on 2022-10-03 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sita', '0005_alter_extractor_itsm_account_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalextractor_itsm',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'sita_extractor_itsm_history'},
        ),
    ]
