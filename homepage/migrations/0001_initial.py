# Generated by Django 3.1.3 on 2020-11-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('availability', models.CharField(max_length=1)),
                ('image', models.CharField(max_length=400)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'items',
                'managed': False,
            },
        ),
    ]
