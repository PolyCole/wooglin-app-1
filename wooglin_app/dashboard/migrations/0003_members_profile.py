# Generated by Django 3.0.7 on 2020-07-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200630_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='profile',
            field=models.CharField(default='default.jpg', max_length=127),
        ),
    ]
