# Generated by Django 4.2.9 on 2024-01-26 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0014_alter_score_panel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='panel',
        ),
    ]
