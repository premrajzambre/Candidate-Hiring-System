# Generated by Django 2.2 on 2020-05-19 16:15

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applicant',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('contact', phone_field.models.PhoneField(blank=True, help_text='Start with country code', max_length=31)),
                ('degree', models.CharField(choices=[('BE/B.Tech', 'BE/B.Tech'), ('ME/M.Tech', 'ME/M.Tech'), ('B.Sc', 'B.Sc'), ('M.Sc', 'M.Sc')], max_length=10)),
                ('degree_score', models.IntegerField(choices=[(60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99)])),
                ('type', models.CharField(choices=[('Fresher', 'Fresher'), ('Experienced', 'Experienced')], max_length=15)),
                ('aptitude_score', models.IntegerField(default=0)),
                ('technical_score', models.IntegerField(default=0)),
                ('personality_score', models.IntegerField(default=0)),
                ('average_score', models.IntegerField(default=0)),
                ('category', models.CharField(blank=True, choices=[('1', 'Selected'), ('0', 'Rejected')], max_length=10, null=True)),
                ('hr_id', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_interview', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
