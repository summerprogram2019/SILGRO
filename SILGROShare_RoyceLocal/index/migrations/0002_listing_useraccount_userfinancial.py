# Generated by Django 2.2.1 on 2019-07-08 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('description', models.TextField()),
                ('availability', models.DateField()),
                ('rate', models.IntegerField()),
                ('images', models.ImageField(upload_to='')),
                ('user_rating', models.IntegerField(default=0, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('user_rating', models.IntegerField(default=0, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserFinancial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40, unique=True)),
                ('card_name', models.CharField(blank=True, max_length=20)),
                ('card_number', models.IntegerField(blank=True, null=True)),
                ('card_expiry', models.DateField(blank=True, null=True)),
                ('card_cvv', models.IntegerField(blank=True, max_length=3, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]