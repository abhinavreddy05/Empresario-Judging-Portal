# Generated by Django 4.2.9 on 2024-01-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0012_remove_score_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='panel',
            field=models.CharField(choices=[('panel1', 'Panel 1'), ('panel2', 'Panel 2')], default=0, max_length=20, null=True),
        ),
    ]