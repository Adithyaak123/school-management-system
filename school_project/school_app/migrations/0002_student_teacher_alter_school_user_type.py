# Generated by Django 5.0 on 2023-12-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=20)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('Address', models.CharField(max_length=50)),
                ('Phone_no', models.CharField(max_length=12)),
                ('user_type', models.CharField(max_length=10)),
                ('value', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=20)),
                ('Phone_no', models.CharField(max_length=12)),
                ('user_type', models.CharField(max_length=10)),
                ('value', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='school',
            name='user_type',
            field=models.CharField(choices=[('1', 'ADMIN'), ('2', 'TEACHER'), ('3', 'STUDENT')], default=1, max_length=10),
        ),
    ]
