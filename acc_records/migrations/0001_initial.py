# Generated by Django 4.0.6 on 2022-10-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('account_money', models.IntegerField()),
                ('account_content', models.TextField()),
                ('account_datetime', models.DateTimeField()),
            ],
        ),
    ]
