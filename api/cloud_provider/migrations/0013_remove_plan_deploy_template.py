# Generated by Django 2.1.2 on 2019-08-02 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_provider', '0012_plan_deploy_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='deploy_template',
        ),
    ]
