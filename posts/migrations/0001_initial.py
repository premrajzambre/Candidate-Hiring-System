# Generated by Django 3.0.5 on 2020-05-24 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('job_title', models.CharField(choices=[('Associate Engineer', 'Associate Engineer'), ('Senior Engineer', 'Senior Engineer'), ('Team Leader', 'Team Leader'), ('Project Architect', 'Project Architect'), ('Project Scrum Master', 'Project Scrum Master'), ('Project Delivery Manager', 'Project Delivery Manager')], max_length=100)),
                ('job_description', models.TextField(max_length=3000)),
                ('skills', models.TextField(max_length=3000)),
                ('thumbnail', models.ImageField(upload_to='thumbnail')),
                ('featured', models.BooleanField()),
                ('experience', models.CharField(choices=[('Fresher', 'Fresher'), ('Experienced', 'Experienced')], max_length=100)),
                ('employment_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], max_length=100)),
                ('vacancy', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('job_status', models.CharField(choices=[('Active', 'Active'), ('Expired', 'Expired')], max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Author')),
                ('next_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='posts.Post')),
                ('previous_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='posts.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
