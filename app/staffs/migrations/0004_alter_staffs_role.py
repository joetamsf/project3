# Generated by Django 3.2.2 on 2022-05-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0003_staffs_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs',
            name='role',
            field=models.CharField(default='member', max_length=10),
        ),
    ]
