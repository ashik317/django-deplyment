# Generated by Django 4.2.4 on 2024-03-10 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='facebool_id',
            new_name='facebook_id',
        ),
    ]
