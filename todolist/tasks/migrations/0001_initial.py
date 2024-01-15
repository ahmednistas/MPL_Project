# Generated by Django 4.2.8 on 2024-01-05 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('ListID', models.IntegerField(primary_key=True, serialize=False)),
                ('LName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.IntegerField(primary_key=True, serialize=False)),
                ('UName', models.CharField(max_length=150)),
                ('UPassword', models.CharField(max_length=150)),
                ('UType', models.IntegerField(choices=[('admin', 'admin'), ('user', 'user')])),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('TaskID', models.IntegerField(primary_key=True, serialize=False)),
                ('TName', models.CharField(max_length=150)),
                ('DueDate', models.DateField(null=True)),
                ('Repeat', models.CharField(choices=[('Daily', 'Daily'), ('Weekdays', 'Weekdays'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=20, null=True)),
                ('Priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=20)),
                ('Status', models.CharField(choices=[('Checked', 'Checked'), ('unChecked', 'unChecked')], default='unChecked', max_length=20)),
                ('Category', models.CharField(choices=[('Blue', 'Blue'), ('Green', 'Green'), ('Orange', 'Orange'), ('Purple', 'Purple'), ('Red', 'Red'), ('Yellow', 'Yellow')], max_length=20, null=True)),
                ('Description', models.CharField(max_length=1000, null=True)),
                ('ListID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.list')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.user')),
            ],
        ),
    ]