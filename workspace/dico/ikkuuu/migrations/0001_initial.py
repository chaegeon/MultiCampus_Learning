# Generated by Django 4.0 on 2021-12-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ikkuuu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatDate', models.DateField()),
                ('writer', models.CharField(max_length=128)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
