# Generated by Django 3.0rc1 on 2019-11-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
