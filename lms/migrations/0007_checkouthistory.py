# Generated by Django 3.0.6 on 2020-05-10 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_auto_20200509_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_out', models.DateTimeField(auto_now_add=True)),
                ('checked_in', models.DateTimeField()),
                ('library_asset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lms.Book')),
                ('library_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lms.LibraryCard')),
            ],
        ),
    ]
