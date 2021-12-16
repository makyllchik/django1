# Generated by Django 4.0 on 2021-12-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('comments', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('text', models.TextField(null=True)),
            ],
        ),
    ]