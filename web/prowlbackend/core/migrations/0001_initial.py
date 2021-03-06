# Generated by Django 2.0.6 on 2018-07-03 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'course code',
                'verbose_name_plural': 'course codes',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(default=0, help_text="The registrar's unique ID.", primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Full course title.', max_length=200)),
                ('users', models.ManyToManyField(related_name='courses', related_query_name='course', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', related_query_name='group', to='core.Course')),
                ('users', models.ManyToManyField(related_name='groups', related_query_name='group', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='code',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', related_query_name='code', to='core.Course'),
        ),
    ]
