# Generated by Django 4.2.2 on 2023-06-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
