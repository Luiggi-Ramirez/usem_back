# Generated by Django 3.2.11 on 2022-09-15 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accidents', '0002_auto_20220908_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='DowntimeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('line_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accidents.linenumber')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
