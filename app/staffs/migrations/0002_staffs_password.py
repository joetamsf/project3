# Generated by Django 3.2.2 on 2022-05-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]