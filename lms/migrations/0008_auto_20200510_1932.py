# Generated by Django 3.0.6 on 2020-05-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0007_checkouthistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkouthistory',
            options={'verbose_name_plural': 'Checkout History'},
        ),
        migrations.AlterField(
            model_name='checkouthistory',
            name='checked_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
