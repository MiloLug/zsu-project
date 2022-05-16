# Generated by Django 4.0.4 on 2022-05-16 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_reasontype_alter_premiumgrid_tariff_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premiumgrid',
            name='tariff_category',
        ),
        migrations.RemoveField(
            model_name='tariffgrid',
            name='position',
        ),
        migrations.AddField(
            model_name='position',
            name='tariff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='general.tariffgrid', verbose_name='Tariff Grid'),
        ),
        migrations.AddField(
            model_name='tariffcategory',
            name='premium_grid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tariff_category', to='general.premiumgrid', verbose_name='Premium Grid'),
        ),
    ]
