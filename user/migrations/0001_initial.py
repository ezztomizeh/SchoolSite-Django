# Generated by Django 3.1 on 2020-08-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Msg_title', models.CharField(default='Untitled', max_length=100)),
                ('Msg_content', models.TextField()),
                ('Msg_sender', models.CharField(max_length=100)),
                ('Msg_reciver', models.CharField(max_length=100)),
            ],
        ),
    ]
