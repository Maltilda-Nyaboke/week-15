# Generated by Django 3.2 on 2022-06-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picwise', '0002_auto_20220607_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
