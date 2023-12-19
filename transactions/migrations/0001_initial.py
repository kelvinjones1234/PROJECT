# Generated by Django 4.2.7 on 2023-11-27 19:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management_app', '0003_department_date_levy_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matriculation_number', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=7)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('paid', models.BooleanField(default=False)),
                ('ref', models.CharField(max_length=20, verbose_name='reference')),
                ('email', models.EmailField(max_length=254)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.department')),
                ('levy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.levy')),
            ],
        ),
    ]
