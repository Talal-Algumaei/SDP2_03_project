# Generated by Django 3.1.1 on 2020-10-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0006_auto_20201013_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashpaneldata',
            name='time_of_print_start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
