# Generated by Django 4.2.5 on 2023-09-26 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=15)),
                ('profesh', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Owner_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('telefon', models.IntegerField()),
                ('breed', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_inspection', models.IntegerField()),
                ('laboratory_tests', models.IntegerField()),
                ('cupping', models.IntegerField()),
                ('haircuts', models.IntegerField()),
                ('nail_trimming', models.IntegerField()),
                ('delivery_reception', models.IntegerField()),
                ('stomat_ment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_inspection', models.TextField(max_length=500)),
                ('laboratory_tests', models.TextField(max_length=500)),
                ('cupping', models.TextField(max_length=500)),
                ('haircuts', models.TextField(max_length=500)),
                ('nail_trimming', models.TextField(max_length=500)),
                ('delivery_reception', models.TextField(max_length=500)),
                ('stomat_ment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.CharField(choices=[('хирург', 'хирург'), ('стоматолог', 'стоматолог'), ('терапевт', 'терапевт'), ('дерматолог', 'дерматолог')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vet_clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servis_price', models.DecimalField(decimal_places=3, max_digits=9)),
                ('animal_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.animal_card')),
                ('breeds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.breed')),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.data')),
                ('doctor', models.ManyToManyField(to='catalog.doctors')),
                ('owner_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.owner_card')),
                ('prices', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.prices')),
                ('services', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.services')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='catalog.status')),
            ],
        ),
    ]
