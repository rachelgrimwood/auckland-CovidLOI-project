# Generated by Django 3.2.6 on 2021-08-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LOIs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('date', models.CharField(max_length=1000)),
                ('time', models.CharField(max_length=1000)),
                ('advice', models.CharField(max_length=1000)),
                ('added', models.CharField(max_length=1000)),
                ('updated', models.CharField(max_length=1000)),
            ],
        ),
    ]
