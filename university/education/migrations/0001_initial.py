# Generated by Django 4.2.3 on 2023-07-20 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplines',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(db_index=True, default=None, null=True)),
                ('name', models.CharField(max_length=150)),
                ('code', models.PositiveSmallIntegerField(unique=True)),
                ('description', models.TextField(null=True)),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specialties',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(db_index=True, default=None, null=True)),
                ('name', models.CharField(max_length=150)),
                ('code', models.PositiveSmallIntegerField(unique=True)),
                ('description', models.TextField(null=True)),
                ('disciplines', models.ManyToManyField(blank=True, related_name='specialties', to='education.disciplines')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(db_index=True, default=None, null=True)),
                ('date_of_admission', models.DateField()),
                ('date_of_expulsion', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_of_admission',),
            },
        ),
        migrations.CreateModel(
            name='StudentGroups',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(db_index=True, default=None, null=True)),
                ('name', models.CharField(max_length=150)),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_groups', to='education.specialties')),
                ('students', models.ManyToManyField(blank=True, related_name='student_groups', to='education.students')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
