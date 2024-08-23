# Generated by Django 5.1 on 2024-08-23 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='area',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.area'),
            preserve_default=False,
        ),
    ]
