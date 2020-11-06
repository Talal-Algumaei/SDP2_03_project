# Generated by Django 3.1.1 on 2020-09-17 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0002_auto_20200830_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashpaneldata',
            name='error_prints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dashpaneldata',
            name='successful_prints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dashpaneldata',
            name='total_print_jobs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dashpaneldata',
            name='number_of_jobs',
            field=models.IntegerField(default=0),
        ),
    ]
