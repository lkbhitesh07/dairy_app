# Generated by Django 3.0.6 on 2020-05-30 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_dairy', '0007_auto_20200530_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerledger',
            name='related_customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_dairy.Profile'),
        ),
    ]
