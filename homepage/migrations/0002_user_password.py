# Generated by Django 3.1.6 on 2021-02-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='test', max_length=25),
            preserve_default=False,
        ),
    ]