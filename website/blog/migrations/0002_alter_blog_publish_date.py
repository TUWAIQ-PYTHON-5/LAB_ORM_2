# Generated by Django 4.1.5 on 2023-02-07 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
