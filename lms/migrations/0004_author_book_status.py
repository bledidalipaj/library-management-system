# Generated by Django 3.0.5 on 2020-04-20 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_auto_20200412_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('AV', 'Available'), ('CO', 'Checked Out'), ('LO', 'Lost')], max_length=2)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_year', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='media')),
                ('number_of_copies', models.IntegerField()),
                ('isbn', models.CharField(max_length=13)),
                ('dewey_index', models.CharField(max_length=15)),
                ('authors', models.ManyToManyField(to='lms.Author')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='lms.LibraryBranch')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='lms.Status')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
