# Generated by Django 4.2.5 on 2023-09-12 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_conversation_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ('-created_at',)},
        ),
    ]
