# Generated by Django 5.0.4 on 2024-04-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_applied', models.CharField(choices=[('Manager', 'Manager'), ('Other', 'Other')], max_length=50)),
                ('about_myself', models.TextField()),
                ('experience', models.CharField(max_length=100)),
                ('experience_years', models.PositiveIntegerField()),
                ('ans1', models.TextField()),
                ('ans2', models.TextField()),
                ('ans3', models.TextField()),
                ('ans4', models.TextField()),
                ('ans5', models.TextField()),
                ('ans6', models.TextField()),
                ('ans7', models.TextField()),
                ('ans8', models.TextField()),
                ('ans9', models.TextField()),
                ('ans10', models.TextField()),
            ],
        ),
    ]