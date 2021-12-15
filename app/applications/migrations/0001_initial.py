# Generated by Django 3.2.8 on 2021-12-13 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0010_remove_property_address1'),
        ('clients', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application_no', models.CharField(max_length=20, unique=True)),
                ('file_no', models.CharField(max_length=20, unique=True)),
                ('received', models.DateField(blank=True, null=True, verbose_name='date received')),
                ('application_type', models.CharField(choices=[('purchase', 'Purchase'), ('lease', 'Lease'), ('lease renewal', 'Lease Renewal')], max_length=20)),
                ('a_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
                ('client', models.ManyToManyField(blank=True, to='clients.Client')),
                ('created_by', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='individualapplication_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='individualapplication_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
