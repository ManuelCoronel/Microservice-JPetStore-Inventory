# Generated by Django 3.2.9 on 2021-11-19 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoy',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank='', default='', upload_to='photos/'),
        ),
    ]
