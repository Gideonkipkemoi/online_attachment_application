# Generated by Django 4.2.5 on 2023-09-22 13:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_apply_expected_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
