# Generated by Django 5.0 on 2024-01-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_remove_job_country_alter_job_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(blank=True, choices=[('All', 'All'), ('Mumbai', 'Mumbai'), ('Bangalore', 'Bangalore'), ('Delhi', 'Delhi'), ('Hyderabad', 'Hyderabad'), ('Chennai', 'Chennai'), ('Lucknow', 'Lucknow')], default='Choose City', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='disability_type',
            field=models.CharField(blank=True, choices=[('All', 'All'), ('Blindness', 'Blindness'), ('Cerebral Palsy', 'Cerebral Palsy'), ('Hearing impairment', 'Hearing impairment'), ('Locomotor disability', 'Locomotor disability'), ('Mental illness', 'Mental illness'), ('Haemophilia', 'Haemophilia')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(blank=True, choices=[('Entry Level', 'Entry Level'), ('1 Year', '1 Year'), ('2 Year', '2 Years'), ('3 Year', '3 Years'), ('4 Year', '4 Years'), ('5 Year', '5+ Years')], max_length=50, null=True),
        ),
    ]
