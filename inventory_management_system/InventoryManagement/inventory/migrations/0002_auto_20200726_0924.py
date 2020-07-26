# Generated by Django 3.0.7 on 2020-07-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Ready to Purchage'), ('SOLD', 'Item Sold'), ('Restocking', 'item restocking in few days')], default='SOLD', max_length=200),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Ready to Purchage'), ('SOLD', 'Item Sold'), ('Restocking', 'item restocking in few days')], default='SOLD', max_length=200),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Ready to Purchage'), ('SOLD', 'Item Sold'), ('Restocking', 'item restocking in few days')], default='SOLD', max_length=200),
        ),
    ]
