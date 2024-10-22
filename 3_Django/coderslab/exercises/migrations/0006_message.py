# Generated by Django 2.0.12 on 2019-08-11 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_auto_20190810_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('od', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Student')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.SchoolSubject')),
            ],
        ),
    ]
