# Generated by Django 4.2.5 on 2023-09-12 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_friendshiprequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected'), ('sent', 'Sent')], default='sent', max_length=20),
        ),
    ]
