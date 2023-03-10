# Generated by Django 4.1.1 on 2022-09-26 07:08

import HmanagerBackend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HmanagerBackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='client_name',
            field=models.CharField(default='widambe', max_length=300),
        ),
        migrations.AddField(
            model_name='booking',
            name='room_payment',
            field=models.IntegerField(default=200000),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HmanagerBackend.roomtype'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_type_pic',
            field=models.ImageField(blank=True, null=True, upload_to=HmanagerBackend.models.upload_path),
        ),
    ]
