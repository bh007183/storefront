# Generated by Django 3.2.7 on 2021-09-27 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customer_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.order'),
        ),
    ]
