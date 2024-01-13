# Generated by Django 5.0 on 2024-01-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact_english', models.CharField(default='none', max_length=400)),
                ('fact_ukrainian', models.CharField(default='none', max_length=400)),
                ('words', models.JSONField(default=dict)),
                ('word_level', models.CharField(default='none', max_length=2)),
            ],
        ),
    ]