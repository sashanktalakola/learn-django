# Generated by Django 5.1.1 on 2024-10-16 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApplication', '0002_user_alter_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
