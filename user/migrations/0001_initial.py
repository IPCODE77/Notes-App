# Generated by Django 4.2.4 on 2023-08-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notepad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_tittle', models.CharField(max_length=500)),
                ('note_desc', models.CharField(max_length=5000)),
            ],
        ),
    ]
