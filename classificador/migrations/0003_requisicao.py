# Generated by Django 2.1.1 on 2018-10-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classificador', '0002_auto_20181025_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
