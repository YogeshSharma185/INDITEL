# Generated by Django 5.1.2 on 2025-02-02 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0014_customerdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateOrderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_currency', models.CharField(max_length=10)),
                ('customer_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customerdetails')),
            ],
        ),
    ]
