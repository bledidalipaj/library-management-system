# Generated by Django 3.0.3 on 2020-02-08 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patron',
            name='libary_card',
        ),
        migrations.AddField(
            model_name='librarycard',
            name='patron',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.Patron'),
        ),
        migrations.AlterField(
            model_name='librarycard',
            name='fees',
            field=models.FloatField(default=0.0),
        ),
    ]
