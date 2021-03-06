# Generated by Django 2.2.7 on 2019-11-25 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bday',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='pass_hash',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='account',
            name='surname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
