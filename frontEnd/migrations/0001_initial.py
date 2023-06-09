# Generated by Django 4.2.1 on 2023-06-03 13:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('OPEN', 'You have opened the task, about to work!'), ('WORKING', 'You are working on the task'), ('DONE', 'You have done the task successfully withing time!'), ('OVERDUE', 'Deadline is crossed')], default='OPEN', max_length=7)),
                ('tags', models.ManyToManyField(to='frontEnd.tags')),
            ],
        ),
    ]
