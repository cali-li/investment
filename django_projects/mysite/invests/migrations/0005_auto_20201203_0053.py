# Generated by Django 3.1.3 on 2020-12-03 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invests', '0004_auto_20201127_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invest',
            name='type',
            field=models.ForeignKey(db_column='type-id', on_delete=django.db.models.deletion.CASCADE, to='invests.type'),
        ),
    ]