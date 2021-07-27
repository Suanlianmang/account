# Generated by Django 3.2.4 on 2021-07-27 11:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('who', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.product')),
            ],
        ),
    ]