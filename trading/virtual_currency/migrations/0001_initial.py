# Generated by Django 2.2.1 on 2019-05-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyHistory',
            fields=[
                ('symbol', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('position', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('price_change_percent', models.FloatField(default=0.0)),
                ('weighted_avg_price', models.FloatField(default=0.0)),
                ('volume', models.FloatField(default=0.0)),
                ('count', models.FloatField(default=0.0)),
                ('saved_date', models.DateTimeField()),
                ('currency_history', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='virtual_currency.CurrencyHistory')),
            ],
        ),
    ]
