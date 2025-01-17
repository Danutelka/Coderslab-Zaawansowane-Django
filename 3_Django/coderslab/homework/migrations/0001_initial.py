# Generated by Django 2.0.12 on 2019-08-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vat', models.IntegerField(choices=[(0, '0'), (1, '0.05'), (2, '0.08'), (3, '0.23')])),
                ('stock', models.IntegerField(default=0)),
                ('categories', models.ManyToManyField(to='homework.Category')),
            ],
        ),
    ]
