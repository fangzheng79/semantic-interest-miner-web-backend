# Generated by Django 2.2.3 on 2020-04-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShortTermInterest',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('keyword', models.CharField(blank=True, max_length=1024, null=True)),
                ('weight', models.IntegerField(default=1)),
                (
                    'source',
                    models.CharField(
                        choices=[
                            ('Twitter', 'Twitter'),
                            ('Scholar', 'Scholar'),
                            ('Manual', 'Manual'),
                        ],
                        default='Manual',
                        max_length=512,
                    ),
                ),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                (
                    'categories',
                    models.ManyToManyField(
                        related_name='short_term_interests', to='interests.Category'
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='LongTermInterest',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('keyword', models.CharField(blank=True, max_length=1024, null=True)),
                ('weight', models.IntegerField(default=1)),
                (
                    'source',
                    models.CharField(
                        choices=[
                            ('Twitter', 'Twitter'),
                            ('Scholar', 'Scholar'),
                            ('Manual', 'Manual'),
                        ],
                        default='Manual',
                        max_length=512,
                    ),
                ),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                (
                    'categories',
                    models.ManyToManyField(
                        related_name='long_term_interests', to='interests.Category'
                    ),
                ),
            ],
        ),
    ]