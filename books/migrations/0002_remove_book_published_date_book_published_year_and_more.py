# Generated by Django 5.0.4 on 2025-05-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
