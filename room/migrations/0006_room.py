# Generated by Django 4.0 on 2022-01-16 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_rename_abcd_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20, null=True, unique=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('r_type', models.CharField(max_length=50, null=True)),
                ('r_image', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]