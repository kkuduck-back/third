# Generated by Django 3.2.9 on 2021-11-28 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defaultsubscription',
            old_name='image',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='image',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='service_id',
            new_name='share_id',
        ),
    ]
