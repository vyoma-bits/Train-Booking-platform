# Generated by Django 5.0 on 2023-12-31 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0015_info_fare1_info_fare2_info_fare3_info_fareg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='user1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('ticket_id', models.CharField(max_length=50)),
            ],
        ),
    ]
