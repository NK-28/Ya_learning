# Generated by Django 4.2 on 2023-04-18 15:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('tournament_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('tournament_type', models.CharField(choices=[('K.O.', 'knockout'), ('group', 'Group')], max_length=200)),
                ('players_number', models.SmallIntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]