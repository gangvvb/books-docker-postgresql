# Generated by Django 4.0.5 on 2022-06-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
