# Generated by Django 4.0.5 on 2022-07-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscriptions', '0007_remove_subscription_amount_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
