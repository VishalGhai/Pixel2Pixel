# Generated by Django 3.1.3 on 2020-12-03 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201203_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default.png', upload_to='pages/profiles'),
        ),
    ]
