# Generated by Django 4.2.5 on 2023-09-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('sent', 'Sent'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='sent', max_length=20),
        ),
    ]