# Generated by Django 3.2.18 on 2023-06-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publica', '0003_auto_20230621_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(default='./perfil/goku.jpg', null=True, upload_to='perfil'),
        ),
    ]
