# Generated by Django 2.2.3 on 2019-07-14 08:12

import address.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0002_auto_20160213_1726'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('cellphone', models.CharField(max_length=10)),
                ('address1', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('address2', address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='address.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]