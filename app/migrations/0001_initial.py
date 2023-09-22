# Generated by Django 4.2.5 on 2023-09-22 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('learning_institution', models.CharField(choices=[('...........', '...........'), ('moi university', 'moi university')], default='...........', max_length=100)),
                ('expected_start_date', models.DateTimeField()),
                ('curriculum_vite', models.FileField(upload_to='cv_uploads')),
                ('recommendation', models.FileField(upload_to='recom_uploads')),
                ('applied_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
            ],
        ),
    ]
