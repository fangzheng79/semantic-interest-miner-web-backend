# Generated by Django 2.2.3 on 2020-04-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('interests', '0007_auto_20200415_1556')]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(blank=True, default='', null=True),
        )
    ]
