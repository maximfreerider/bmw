# Generated by Django 2.0.7 on 2018-08-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='mukola',
            field=models.CharField(blank=True, default=None, max_length=12, null=True),
        ),
    ]