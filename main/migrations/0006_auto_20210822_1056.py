# Generated by Django 3.2.6 on 2021-08-21 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210822_0135'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LOIModelNew',
        ),
        migrations.AddField(
            model_name='loimodel',
            name='updated',
            field=models.IntegerField(default=1),
        ),
    ]
