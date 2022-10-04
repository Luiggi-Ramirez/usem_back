# Generated by Django 3.2.11 on 2022-10-03 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accidents', '0002_auto_20220908_1754'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenderCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='headcount.gendercatalog')),
            ],
        ),
        migrations.CreateModel(
            name='PeopleOnTurn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accidents.area')),
                ('business_unity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accidents.businessunity')),
                ('line_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accidents.linenumber')),
                ('turn', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accidents.turns')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='headcount.worker')),
            ],
        ),
    ]