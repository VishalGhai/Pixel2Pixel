# Generated by Django 3.1.3 on 2020-12-07 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201203_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default.png', upload_to='static/project1'),
        ),
    ]
