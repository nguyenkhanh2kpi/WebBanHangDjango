# Generated by Django 3.1.14 on 2022-05-13 07:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20220513_1457'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0003_order_order_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='is_completed',
            new_name='paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_description',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_total',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 5, 13, 7, 57, 32, 582173, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='product.product')),
            ],
        ),
    ]
