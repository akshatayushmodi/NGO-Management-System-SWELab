# Generated by Django 4.1.7 on 2023-03-30 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0008_alter_pledge_donor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='did',
        ),
    ]