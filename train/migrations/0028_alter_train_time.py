# Generated by Django 5.0 on 2024-01-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0027_rename_ticket_id_user1_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
