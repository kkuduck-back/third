# Generated by Django 3.2.9 on 2021-11-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
