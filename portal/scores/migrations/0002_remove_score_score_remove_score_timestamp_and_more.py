# Generated by Django 4.2.1 on 2023-06-05 18:24

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0006_remove_participant_drive_file_id_and_more'),
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='score',
        ),
        migrations.RemoveField(
            model_name='score',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='score',
            name='judge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customUser.judge'),
        ),
        migrations.AddField(
            model_name='score',
            name='parameters',
            field=jsonfield.fields.JSONField(default='', null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customUser.participant'),
        ),
    ]