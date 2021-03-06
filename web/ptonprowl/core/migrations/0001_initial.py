<<<<<<< Updated upstream:web/ptonprowl/core/migrations/0001_initial.py
# Generated by Django 2.0.6 on 2018-06-19 19:59
=======
# Generated by Django 2.0.6 on 2018-06-19 19:33
>>>>>>> Stashed changes:web/ptonprowl/courses_groups/migrations/0001_initial.py

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('code', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('groups', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Course')),
            ],
        ),
        migrations.AddField(
            model_name='code',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Course'),
        ),
    ]
