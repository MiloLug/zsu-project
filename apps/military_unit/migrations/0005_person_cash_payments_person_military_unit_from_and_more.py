# Generated by Django 4.0.4 on 2022-05-20 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_remove_premiumgrid_tariff_category_and_more'),
        ('military_unit', '0004_remove_staff_military_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cash_payments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='general.tariffgrid', verbose_name='Tariff'),
        ),
        migrations.AddField(
            model_name='person',
            name='military_unit_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='persons_who_come_from', to='military_unit.militaryunit', verbose_name='Military Unit where did come from'),
        ),
        migrations.AddField(
            model_name='person',
            name='place_of_residence',
            field=models.CharField(default=0, max_length=255, verbose_name='Place of residence'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='type_of_contract',
            field=models.CharField(choices=[('мобілізація', 'Mobilization'), ('строкова служба', 'Conscription'), ('контракт', 'Contract')], default=1, max_length=100, verbose_name='Type of contract'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='vacation',
            field=models.BooleanField(default=False, verbose_name='Vacation'),
        ),
        migrations.AddField(
            model_name='person',
            name='vacation_days',
            field=models.IntegerField(default=1, verbose_name='Vacation days'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='family_status',
            field=models.CharField(choices=[('одружений', 'Married Man'), ('неодружений', 'Not Married Man'), ('заміжня', 'Married Woman'), ('незаміжня', 'Not Married Woman'), ('розлучений', 'Divorced Man'), ('розлучена', 'Divorced Woman'), ('вдова', 'Widow'), ('вдівець', 'Widower')], max_length=255, verbose_name='Family status'),
        ),
    ]
