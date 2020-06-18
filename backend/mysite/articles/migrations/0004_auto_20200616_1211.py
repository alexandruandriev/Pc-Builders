# Generated by Django 3.0.7 on 2020-06-16 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200616_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ram',
            name='prduct_code',
            field=models.FilePathField(max_length=40),
        ),
        migrations.AlterField(
            model_name='ram',
            name='size',
            field=models.CharField(choices=[('2', '2GB'), ('4', '4GB'), ('8', '8GB'), ('16', '16GB'), ('32', '32GB'), ('64', '64GB'), ('124', '124GB')], max_length=3),
        ),
    ]