# Generated by Django 2.0.6 on 2018-06-19 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('number', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('groups', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_groups.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_groups.Course')),
            ],
        ),
    ]