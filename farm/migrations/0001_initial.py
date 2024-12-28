# Generated by Django 5.1.4 on 2024-12-28 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cow',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm.animal')),
                ('milk_yield', models.FloatField()),
            ],
            bases=('farm.animal',),
        ),
        migrations.CreateModel(
            name='Pig',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm.animal')),
                ('weight', models.IntegerField()),
            ],
            bases=('farm.animal',),
        ),
        migrations.CreateModel(
            name='Sheep',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='farm.animal')),
                ('wool_color', models.CharField(max_length=50)),
            ],
            bases=('farm.animal',),
        ),
        migrations.AddField(
            model_name='animal',
            name='farm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='farm.farm'),
        ),
    ]
