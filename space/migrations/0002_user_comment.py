# Generated by Django 3.0.8 on 2020-08-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
    ]
