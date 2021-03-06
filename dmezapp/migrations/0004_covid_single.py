# Generated by Django 3.1 on 2020-12-31 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmezapp', '0003_best'),
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(default='', max_length=50)),
                ('mrp_price', models.FloatField()),
                ('price', models.FloatField()),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('digital', models.NullBooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(default='', upload_to='pics')),
            ],
        ),
    ]
