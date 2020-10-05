# Generated by Django 3.1.2 on 2020-10-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('role_id', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
