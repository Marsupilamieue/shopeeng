# Generated by Django 4.2.5 on 2023-09-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
