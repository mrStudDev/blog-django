# Generated by Django 3.1.4 on 2020-12-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('categoria', models.CharField(max_length=30)),
                ('conteudo', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
