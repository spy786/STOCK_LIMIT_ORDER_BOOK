# Generated by Django 4.2.17 on 2025-01-31 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0005_alter_stoploss_order_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoploss_order',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
