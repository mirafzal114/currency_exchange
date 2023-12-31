# Generated by Django 5.0 on 2023-12-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransferFrom', models.CharField(max_length=100)),
                ('TransferTo', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('conversion_result', models.DecimalField(decimal_places=2, max_digits=30)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
