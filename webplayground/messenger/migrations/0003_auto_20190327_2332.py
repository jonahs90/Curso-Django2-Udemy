# Generated by Django 2.0.2 on 2019-03-27 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_thread_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['updated']},
        ),
    ]