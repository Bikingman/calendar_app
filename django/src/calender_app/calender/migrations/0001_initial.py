# Generated by Django 3.1 on 2020-08-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
