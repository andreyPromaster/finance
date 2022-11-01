# Generated by Django 4.1.2 on 2022-10-18 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_bankdetails_company_bank_detail'),
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='type',
            field=models.CharField(choices=[('Поступление', 'Поступление'), ('Расходы', 'Расходы')], default='Поступление', max_length=15, verbose_name='Тип счета'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='bank_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.bankdetails'),
        ),
        migrations.AlterField(
            model_name='paymentitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_items', to='bill.invoice'),
        ),
        migrations.DeleteModel(
            name='BankDetails',
        ),
    ]