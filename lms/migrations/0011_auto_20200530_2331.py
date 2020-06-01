# Generated by Django 3.0.6 on 2020-05-30 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0010_auto_20200523_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='patron',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='librarycard',
            name='patron',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='library_card', to='lms.Patron'),
        ),
    ]