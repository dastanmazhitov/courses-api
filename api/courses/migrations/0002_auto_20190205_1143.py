# Generated by Django 2.1.5 on 2019-02-05 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='course',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='course',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]