# Generated by Django 4.0.5 on 2022-07-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscriptions', '0009_alter_subscription_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequency',
            name='slug',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
