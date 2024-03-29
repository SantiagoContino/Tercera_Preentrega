# Generated by Django 5.0.1 on 2024-01-15 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderapp', '0002_curso_entregable_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crossover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deportivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Urban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
