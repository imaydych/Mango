# Generated by Django 2.2.3 on 2019-11-06 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mango', '0013_auto_20191030_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangoabout',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MangoAbouts', to=settings.AUTH_USER_MODEL),
        ),
    ]
