# Generated by Django 2.2.24 on 2022-09-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20220913_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(verbose_name='Текст жалобы'),
        ),
    ]
