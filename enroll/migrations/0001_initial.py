# Generated by Django 5.1.4 on 2025-01-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=20)),
                ('stuemail', models.EmailField(max_length=30)),
                ('stupass', models.CharField(max_length=40)),
            ],
        ),
    ]
