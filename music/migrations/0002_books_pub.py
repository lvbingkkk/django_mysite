# Generated by Django 5.0 on 2023-04-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='pub',
            field=models.CharField(default='', max_length=100, verbose_name='出版社'),
        ),
    ]
