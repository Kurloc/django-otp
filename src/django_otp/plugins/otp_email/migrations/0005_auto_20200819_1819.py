# Generated by Django 3.1 on 2020-08-19 23:19

from django.db import migrations, models
import django_otp.plugins.otp_email.models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_email', '0004_throttling'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaildevice',
            name='key',
            field=models.CharField(default=django_otp.plugins.otp_email.models.default_key, help_text='A hex-encoded secret key of up to 40 bytes.', max_length=80, validators=[django_otp.plugins.otp_email.models.key_validator]),
        ),
    ]
