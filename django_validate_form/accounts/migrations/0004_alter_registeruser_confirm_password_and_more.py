# Generated by Django 5.0.4 on 2024-04-30 06:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_registeruser_remove_user_confirm_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='confirm_password',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(5, message='Min Length of Confirm Password is 5 letters')], verbose_name='Confirm Password'),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='password',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(5, message='Min Length of Password is 5 letters')], verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='postal_code',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000, message='Postal code must be greater than equal to 1000.'), django.core.validators.MaxValueValidator(99999, message='Postal code must be lesser than equal to 99999.')], verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(5, message='Min Length of User Name is 5 letters!')], verbose_name='User Name'),
        ),
    ]