# Generated by Django 4.0.3 on 2022-03-20 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.URLField(default='https://github.com/mdo.png'),
            preserve_default=False,
        ),
    ]
