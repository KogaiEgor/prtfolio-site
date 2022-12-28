# Generated by Django 4.1.3 on 2022-12-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]