# Generated by Django 5.0 on 2023-12-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0007_alter_train_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('id_1', models.IntegerField()),
                ('date', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='train',
            name='seats',
            field=models.IntegerField(),
        ),
    ]
