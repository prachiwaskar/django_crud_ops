# Generated by Django 3.2.6 on 2021-08-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STUDENT_NO', models.IntegerField()),
                ('STUDENT_NAME', models.CharField(max_length=30)),
                ('STUDENT_DOB', models.DateField()),
                ('STUDENT_DOJ', models.DateField()),
            ],
        ),
    ]