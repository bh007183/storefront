# Generated by Django 3.2.7 on 2021-09-27 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210927_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='store.order'),
        ),
    ]
