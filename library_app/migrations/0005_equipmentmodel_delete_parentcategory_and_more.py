# Generated by Django 5.0.7 on 2024-08-26 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=200)),
                ('equip_model_name', models.CharField(max_length=200)),
                ('equip_model_id', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='./static/images/model')),
            ],
        ),
        migrations.DeleteModel(
            name='ParentCategory',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='equip_model_id',
            new_name='equip_location_id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='equipmentmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.category'),
        ),
    ]
