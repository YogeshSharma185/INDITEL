# Generated by Django 5.0.2 on 2024-06-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_alter_postpaid_data_rollover_alter_postpaid_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='prepaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prepaid_name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('sub_category', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
