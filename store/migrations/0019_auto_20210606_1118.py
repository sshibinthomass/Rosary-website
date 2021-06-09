# Generated by Django 3.2 on 2021-06-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_product_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(choices=[('None', 'None'), ('On Offer', 'On Offer'), ('Fast Selling', 'Fast Selling'), ('New', 'New')], default='None', max_length=20),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
