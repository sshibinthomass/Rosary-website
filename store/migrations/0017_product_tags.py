# Generated by Django 3.2 on 2021-06-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_product_maintenance'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(choices=[('none', 'None'), ('offer', 'On Offer'), ('fast', 'Fast Selling'), ('new', 'New')], default='none', max_length=20),
        ),
    ]
