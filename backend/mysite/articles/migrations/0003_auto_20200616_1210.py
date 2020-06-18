# Generated by Django 3.0.7 on 2020-06-16 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_ram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ram',
            name='frequency',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ram',
            name='size',
            field=models.FilePathField(choices=[('2', '2GB'), ('4', '4GB'), ('8', '8GB'), ('16', '16GB'), ('32', '32GB'), ('64', '64GB'), ('124', '124GB')], max_length=3),
        ),
    ]